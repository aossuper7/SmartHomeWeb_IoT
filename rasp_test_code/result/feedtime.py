from time import *
from feedservo import Feed_Servo
from email.utils import localtime
import time
from threading import Thread
import paho.mqtt.publish as publisher

class feedTime(Thread):
    def __init__(self):
        super().__init__()
        self.feedmypet = Feed_Servo()
        self.setTime1 = "07:00:00"
        self.setTime2 = "12:00:00"

    def setfeedtime(self, setTime1, setTime2):
        self.setTime1 = str(setTime1) + ":00"
        self.setTime2 = str(setTime2) + ":00"
        print(self.setTime1)
        print(self.setTime2)

    def run(self):
        try:
            while True:
                now = localtime()
                myhour = str(now.hour)
                mymin = str(now.minute)
                mysec = str(now.second)

                if now.hour < 10:
                    myhour = "0" + str(now.hour)
                if now.minute < 10:
                    mymin = "0" + str(now.minute)
                if now.second < 10:
                    mysec = "0" + str(now.second)
                cur_time = myhour + ":" + mymin + ":" + mysec
                time.sleep(1)
                if cur_time == (self.setTime1) or cur_time == (self.setTime2):
                    self.feedmypet.dooropen()
                    print("사료오쁜")
                    time.sleep(5)
                    self.feedmypet.doorclose()
                    print("사료닫힘")
                publisher.single("iot/timechk",str(self.setTime1) + "/" + str(self.setTime2),hostname="192.168.0.2")
        except KeyboardInterrupt:
            pass
        finally:
            pass

    def manualrun(self):
        self.feedmypet.dooropen()
        time.sleep(5)
        self.feedmypet.doorclose()
