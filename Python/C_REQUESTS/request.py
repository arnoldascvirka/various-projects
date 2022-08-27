from datetime import datetime
import requests
import json
import time

API_key = "668424706068268978818x70951"
COORD_LINK = "https://geocode.xyz/"
COORD_PAYLOAD = {"json": "1", "key": API_key}
WEATHER_LINK = "https://api.open-meteo.com/v1/forecast"


def koordinaciu_uzklausa(valandos, *miestai, link=COORD_LINK, param=COORD_PAYLOAD):
    time.sleep(2)
    for i in miestai:
        try:
            r = requests.get(f"{link}{i}", params=param)
            print(i)
            koordinates(r.text, valandos)
        except ConnectionError:
            print("GEOCODE Connection Error")


def koordinates(info, valandos):
    geo_d = json.loads(info)
    latt_ = geo_d["latt"]
    longt_ = geo_d["longt"]
    temperaturos_uzklausa(latt_, longt_, valandos)


def temperaturos_uzklausa(lat, longt, valandos, link=WEATHER_LINK):
    time.sleep(2)
    weather_payload = {"latitude": lat, "longitude": longt, "hourly": "temperature_2m"}
    try:
        r = requests.get(link, params=weather_payload)
        temperaturos(r.text, valandos)
    except ConnectionError:
        print("OPEN-METEO Connection Error")


def temperaturos(info, valandos):
    res = json.loads(info)
    atskaita = res["hourly"]["time"].index(datetime.now().strftime("%Y-%m-%dT%H:00"))
    laikai = res["hourly"]["time"][atskaita : atskaita + valandos]
    temperaturos = res["hourly"]["temperature_2m"][atskaita : atskaita + valandos]
    for date, temp in zip(laikai, temperaturos):
        print(f"\t{date[:10]} {date[11:]}val Temperatūra: {temp}°C")


koordinaciu_uzklausa(10, "Kaunas", "Vilnius", "Klaipeda", "Alytus")
