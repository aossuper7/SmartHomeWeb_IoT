from threading import Thread
import paho.mqtt.publish as publish
import time
import board  # 데이터 송신용 board모듈
import adafruit_dht
import os
import fcntl

I2C_SLAVE = 0x703
PM2008 = 0x28


class SEN(Thread):
    def __init__(self):
        super().__init__()
        self.mydht11 = adafruit_dht.DHT11(board.D13)
        self.fd = os.open('/dev/i2c-1', os.O_RDWR)
        self.io = fcntl.ioctl(self.fd, I2C_SLAVE, PM2008)

    def run(self):
        while True:
            try:
                humidity_data = self.mydht11.humidity
                temperature_data = self.mydht11.temperature
                dust_temp = os.read(self.fd, 32)
                dust_data = 256 * int(dust_temp[9]) + int(dust_temp[10])
                publish.single("android/dht",
                               "hu:" + str(humidity_data) + ":" + str(temperature_data) + ":" + str(dust_data),
                               hostname="192.168.0.2")
                print(humidity_data, temperature_data, dust_data)
                time.sleep(4.8)
            except RuntimeError as error:
                print(error.args[0])
            finally:
                pass