import requests
import xml.etree.ElementTree as ET
from ics import Calendar, Event
from datetime import datetime

XML_URL = "https://zerodha.com/marketintel/bulletin/?format=xml"

xml_data = requests.get(XML_URL).text
root = ET.fromstring(xml_data)

cal = Calendar()

for item in root.findall(".//holiday"):
    e = Event()
    e.name = item.find("title").text
    e.begin = datetime.strptime(item.find("date").text, "%Y-%m-%d")
    cal.events.add(e)

with open("calendar.ics", "w") as f:
    f.writelines(cal)

print("ICS generated")
