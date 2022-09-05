from threading import Thread
import paho.mqtt.publish as publish
import RPi.GPIO as g
import time


class Pir(Thread):
    def __init__(self, rfid, buzzer):
        super().__init__()
        self.rfid = rfid
        self.pirPin = 5
        self.blueLED = 20
        self.redLED = 21
        self.buzzerStart = buzzer
        g.setmode(g.BCM)
        g.setup(self.pirPin, g.IN)
        g.setup(self.blueLED, g.OUT)
        g.setup(self.redLED, g.OUT)

    def warning(self):
        for i in range(10):
            self.buzzerStart.buzzerOn()
            g.output(self.blueLED, g.HIGH)
            time.sleep(0.5)
            g.output(self.blueLED, g.LOW)
            g.output(self.redLED, g.HIGH)
            time.sleep(0.5)
            g.output(self.redLED, g.LOW)

    def run(self):
        while True:
            if self.rfid.access_state['person'] == 0:
                if g.input(self.pirPin) == 1:
                    publish.single("android/pir", "warning", hostname="192.168.0.2")
                    print("허가되지 않은 사람 감지")
                    self.warning()
                    self.buzzerStart.buzzerOff()