from email.utils import localtime
import RPi.GPIO as gpio
from time import *
import time


class Feed_Servo:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.servo_pin = 18
        gpio.setup(self.servo_pin, gpio.OUT)
        self.pwm = gpio.PWM(self.servo_pin, 50)
        self.pwm.start(0)

    def dooropen(self):
        self.pwm.ChangeDutyCycle(13)

    def doorclose(self):
        self.pwm.ChangeDutyCycle(3)

    def clean(self):
        gpio.cleanup()