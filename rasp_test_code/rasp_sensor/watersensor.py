from threading import Thread
from pyfirmata import  Arduino,util
import RPi.GPIO as GPIO
import time
from threading import Thread
import paho.mqtt.publish as publisher


class myWater(Thread):
    def __init__(self):
        super().__init__()
        board = Arduino("/dev/ttyACM1")
        self.pin_water = board.get_pin("a:0:i")
        self.pin_pumpA1 = board.get_pin("d:6:o")
        self.pin_pumpA2 = board.get_pin("d:7:o")
           
        it = util.Iterator(board)
        it.start()
        self.pin_water.enable_reporting() 
                   
    def run(self):
        try:
            while True:
                val = self.pin_water.read()
                print("waterval: "+str(val)) 
                publisher.single("mypet/waterlevel", val, hostname="172.30.1.58")
                time.sleep(2)
                if val!=None:
                    print(float(val))
                    if float(val) < 0.4 :
                        self.pin_pumpA1.write(1)
                        self.pin_pumpA2.write(0)
                        time.sleep(5)
                    else:
                        self.pin_pumpA1.write(0)
                        self.pin_pumpA2.write(0)               
        except KeyboardInterrupt:
            pass
        finally:
            pass
    def manualrun(self):
        print("ooooooooo")
        self.pin_pumpA1.write(1)
        self.pin_pumpA2.write(0)
        time.sleep(5)
        self.pin_pumpA1.write(0)
        self.pin_pumpA2.write(0)

