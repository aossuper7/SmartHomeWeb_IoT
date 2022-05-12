from threading import Thread
import paho.mqtt.client as mqtt
import time
from feedservo import Feed_Servo
from watersensor import myWater
from feedtime import feedTime

class mymqttworker:
    def __init__(self, topic):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_msg
        self.topic = topic 
        self.mypetfeed = feedTime()
        self.mypetfeed.start()
        self.waterSensor = myWater()
        self.waterSensor.start()
        
    def on_connect(self, client, userdata, flage, rc):
        print("connecting"+str(rc))
        if rc == 0: #성공
            client.subscribe(self.topic)
            time.sleep(1)
        else:
            print("connection fail")
    def on_msg(self, client, userdata, message):
        memo = message.payload.decode("utf-8")
        print(message.topic+" "+memo)
        if message.topic == "mypet/feed":
            print("도어오픈")
            self.mypetfeed.manualrun()
        elif message.topic == "mypet/water":
            print("워터오픈")
            self.waterSensor.manualrun()
        elif message.topic == "mypet/setTime":
            timearray = memo.split("/")
            self.mypetfeed.setfeedtime(timearray[0], timearray[1])

    def working(self):
        try:
            self.client.connect("172.30.1.56", 1883, 60)
            obj = Thread(target=self.client.loop_forever)
            obj.start()
        except KeyboardInterrupt:
            pass
        finally:
            pass