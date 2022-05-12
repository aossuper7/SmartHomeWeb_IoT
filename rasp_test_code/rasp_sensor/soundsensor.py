from threading import Thread
import paho.mqtt.publish as pub
import time
import RPi.GPIO as gpio

class mySound(Thread):
    def __init__(self):
        super().__init__()
        self.sound = 19
        gpio.setmode(gpio.BCM)
        gpio.setup(self.sound, gpio.IN)
    def run(self):
        while True:
            if gpio.input(self.sound) == 1 :
                print("큰 소리가 감지됨", self.count)
                pub.single("iot/sound", "alert", hostname="172.30.1.56")
            else:
                print(gpio.input(self.sound), self.count)

            
            time.sleep(2)

