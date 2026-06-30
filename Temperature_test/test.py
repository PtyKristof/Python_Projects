import random
import time
from datetime import datetime


class Sensor:
    def __init__(self, min_temp: float = 20.0, max_temp: float = 60.0):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def read(self) -> float:
        return random.uniform(self.min_temp, self.max_temp)

def log_readings(sensor: Sensor, count: int, interval: float) -> list[float]:
    readings = []
    for i in range(count):
        value = sensor.read()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} -> {value:.2f} °C")
        readings.append(value)
        if i < count - 1:
            time.sleep(interval)
    return readings     

if __name__ == "__main__":
    sensor = Sensor()
    data = log_readings(sensor, count=5, interval=1)

    average = sum(data) / len(data)
    maximum = max(data)

    print(f"\nÁtlag: {average:.2f} °C")
    print(f"Maximum: {maximum:.2f} °C")