#!/usr/bin/env python3

import urllib.request
import json
from datetime import datetime

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=41.8781"
    "&longitude=-87.6298"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

try:
    with urllib.request.urlopen(url, timeout=30) as response:
        data = json.loads(response.read().decode())

    current = data["current"]

    print("================================")
    print("       DAILY WEATHER REPORT")
    print("================================")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind Speed:", current["wind_speed_10m"], "km/h")
    print("================================")

except Exception as error:
    print("Weather report failed:", error)
