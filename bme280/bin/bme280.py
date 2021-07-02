import board
from adafruit_bme280 import basic as adafruit_bme280

import json
import time

i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)

data = {
    "temperature": round(bme280.temperature, 1),
    "pressure": round(bme280.pressure, 1),
    "humidity": round(bme280.humidity, 1),
    "timestamp": int(time.time())
    }

with open("www/data.json", "w") as file:
    json.dump(data, file);
