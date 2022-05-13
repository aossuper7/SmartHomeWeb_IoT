from time import *
from feedservo import Feed_Servo
from email.utils import localtime
import time
from threading import Thread


class feedTime(Thread):
    def __init__(self):
        super().__init__()
        self.feedmypet = Feed_Servo()
        self.setTime1 = "7:0:0"
        self.setTime2 = "12:0:0"
        
        
    def setfeedtime(self, setTime1, setTime2):
        self.setTime1 = str(setTime1)+":0"
        self.setTime2 = str(setTime2)+":0"
        print(self.setTime1)
        print(self.setTime2)
        
    def run(self):
        try:
            while True:
                now = localtime()
                cur_time = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
                # print(cur_time)
                if cur_time == (self.setTime1) or cur_time == (self.setTime2):
                    self.feedmypet.dooropen()
                    print("사료오쁜")
                    time.sleep(5)
                    self.feedmypet.doorclose()
                    print("사료닫힘")
        except KeyboardInterrupt:
            pass
        finally:
            pass
    def manualrun(self):
        self.feedmypet.dooropen()
        time.sleep(5)
        self.feedmypet.doorclose()