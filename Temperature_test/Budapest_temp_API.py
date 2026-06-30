#Valós idejű adatokat kérünk le a netről és így írjuk ki Budapest (latitude=47.484734; longitude=19.02533) hőmérsékletét
#24 elemű string a mai nap hőmérsékleteivel óránként, az adott óráig a pontosat írja, utána lévők pedig előrejelzés

import requests
import time
from datetime import datetime


def get_hourly_temperatures(lat=47.4979, lon=19.0402):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "forecast_days": 1
    }
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data["hourly"]["time"], data["hourly"]["temperature_2m"]


class WeatherSensor:
    def __init__(self, lat=47.4979, lon=19.0402):  # ha változtatni akarunk koordinátát itt kell
        self.lat = lat
        self.lon = lon

    def read(self):
        return get_hourly_temperatures(self.lat, self.lon)


if __name__ == "__main__":
    sensor = WeatherSensor()
    timestamps, temperatures = sensor.read()

    for t, temp in zip(timestamps, temperatures):
        print(f"{t} -> {temp:.2f} °C")

    average = sum(temperatures) / len(temperatures)
    maximum = max(temperatures)
    minimum = min(temperatures)

    print(f"\nÁtlag: {average:.2f} °C")
    print(f"Maximum: {maximum:.2f} °C")
    print(f"Minimum: {minimum:.2f} °C")