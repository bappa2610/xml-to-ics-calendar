import requests
import xml.etree.ElementTree as ET
from ics import Calendar, Event
from datetime import datetime

XML_URL = "https://zerodha.com/marketintel/holiday-calendar/?format=xml"

response = requests.get(XML_URL)
response.raise_for_status()

root = ET.fromstring(response.content)
calendar = Calendar()

# Zerodha XML structure
for holiday in root.findall(".//holiday"):
    name = holiday.findtext("description")
    date = holiday.findtext("date")

    if not name or not date:
        continue

    event = Event()
    event.name = name
    event.begin = datetime.strptime(date, "%Y-%m-%d")
    event.make_all_day()

    calendar.events.add(event)

with open("calendar.ics", "w", encoding="utf-8") as f:
    f.writelines(calendar)

print("Zerodha holiday calendar updated successfully")
