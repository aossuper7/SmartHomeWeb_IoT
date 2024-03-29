import threading
import paho.mqtt.publish as publisher
from threading import Event

import sys, os

sys.path.append("/home/pi/mywork/basic/result")
from timechk1 import timechk1


class camerapub(threading.Thread):
    def __init__(self, camera):
        threading.Thread.__init__(self)
        self.exit_event = Event()
        self.camera = camera
        self.timechk = timechk1()

    def run(self):
        self.timechk.start()
        while True:
            frame = self.camera.getStreaming()
            publisher.single("iot/mycamera", frame, hostname="192.168.0.2")
            if self.timechk.count == 1:
                self.timechk.count = 0
                break

