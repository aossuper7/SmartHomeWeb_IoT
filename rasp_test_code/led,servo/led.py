import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


class LED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.led_pin = 22
        GPIO.setup(self.led_pin,GPIO.OUT) 
        
    def led_on(self):
        GPIO.output(self.led_pin,GPIO.HIGH)
        
    def led_off(self):
        GPIO.output(self.led_pin,GPIO.LOW)
        
    def clean(self):
        GPIO.cleanup()