from logging.config import valid_ident
from threading import Thread
from pyfirmata import  Arduino,util
import paho.mqtt.publish as pub
import time
import RPi.GPIO as gpio

class mySound(Thread):
    def __init__(self):
        super().__init__()
        board = Arduino("/dev/ttyACM1")
        self.pin_sound = board.get_pin("a:1:i")

        it = util.Iterator(board)
        it.start()
        self.pin_sound.enable_reporting()
    def run(self):
        while True:
            val = self.pin_sound.read()
            print("soundval:"+str(val))
            # if gpio.input(self.sound) == 1 :
            #     print("큰 소리가 감지됨")
            #     pub.single("iot/sound", "alert", hostname="172.30.1.58")
            # else:
            #     pass

            time.sleep(2)


