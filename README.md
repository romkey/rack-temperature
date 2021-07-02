# rack-temperature

This is a simple script and web page that reads the temperature inside the computer rack at [PDX Hackerspace](https://pdxhackerspace.org) and reports it via a web page.

## Hardware

This is intended to run on a Raspberry Pi with a [BME280](https://www.adafruit.com/product/2652) wired up to its first I2C port via the GPIO pins.

You can choose from many different sensors but you'll obviously need to adapt the code if you want to use a different sensor. You should be able to use a BME280 from any vendor without modifying the code, not just Adafruit's. But support Adafruit.

