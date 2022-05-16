from email.utils import localtime
import RPi.GPIO as gpio
from time import *
import time

class Feed_Servo:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.servo_pin = 26
        gpio.setup(self.servo_pin, gpio.OUT)
        self.pwm = gpio.PWM(self.servo_pin, 50)
        self.pwm.start(3)
    def dooropen(self):
        self.pwm.ChangeDutyCycle(13)
        time.sleep(0.02)
    def doorclose(self):
        self.pwm.ChangeDutyCycle(3)
        time.sleep(0.02)
    def clean(self):
        gpio.cleanup()