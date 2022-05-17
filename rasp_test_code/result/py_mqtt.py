import paho.mqtt.client as client
import paho.mqtt.publish as publisher
from camerapub_thread import camerapub
from camerapub import Mycamera
from threading import Event
import RPi.GPIO as gpio
from led import LED
from watersensor import myWater
from servo import Servo
import signal
import threading
from distance import mydis
from feedservo import Feed_Servo
from feedtime import feedTime


class cameramqtt:
    def __init__(self):
        self.client = client.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.exit_event = Event()

        # 카메라
        self.camera = Mycamera()
        self.camerachkcnt = 0

        # 거리
        self.distance = mydis(self.client)
        self.distance.start()

        # 펫 먹이 시간
        self.mypetfeed = feedTime()
        self.mypetfeed.start()

        # 펫 물 시간
        # self.waterSensor = myWater()
        # self.waterSensor.start()

        # led
        self.led = LED()

        # servo
        self.curtain = Servo()

    def signal_handler(self, signum, frame):
        self.exit_event.set()
        gpio.cleanup()
        if self.exit_event.is_set() == True:
            exit(0)

    def mqtt_connect(self):
        try:
            self.client.connect("192.168.0.24", 1883, 60)
            signal.signal(signal.SIGINT, self.signal_handler)
            mythreadobj = threading.Thread(target=self.client.loop_forever)
            mythreadobj.start()

        except KeyboardInterrupt:
            pass
        finally:
            print("종료")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("연결 완료")
            client.subscribe("iot/#")
            client.subscribe("camerachk")
            client.subscribe("pi/#")
            client.subscribe("mypet/#")
        else:
            print("연결 실패")

    def on_message(self, client, userdate, message):
        try:
            cameval = message.payload.decode("utf-8")

            # 카메라 체크
            if (message.topic == "camerachk"):
                if cameval == "start" and self.camerachkcnt == 0:
                    self.camerapub = camerapub(self.camera)
                    self.camerachkcnt = 1
                    self.camerapub.start()
                elif cameval == "stop":
                    self.camerapub.timechk.count = 1
                    self.camerachkcnt = 0
            # led
            elif (message.topic == "iot/led"):
                if cameval == "led_on":
                    self.led.led_on()
                elif cameval == "led_off":
                    self.led.led_off()
            # 커튼
            elif message.topic == "iot/servo":
                if cameval == "servo_open":
                    self.curtain.servo_open()
                elif cameval == "servo_close":
                    self.curtain.servo_close()

            # 펫 먹이
            elif message.topic == "mypet/feed":
                print("도어 오픈")
                self.mypetfeed.manualrun()

            # 펫 물주기
            elif message.topic == "mypet/water":
                print("물주기 동작")
                self.waterSensor.manualrun()

            # 시간 설정
            elif message.topic == "mypet/setTime":
                timearray = cameval.split("/")
                self.mypetfeed.setfeedtime(timearray[0], timearray[1])

            elif message.topic == "mypet/setTimeA":
                timearray = cameval.split("/")
                time1 = timearray[0].split(":")
                time2 = timearray[1].split(":")
                time1_hour = time1[0]
                time1_min = time1[1]
                time2_hour = time2[0]
                time2_min = time2[1]
                if int(time1_hour) < 10:
                    time1_hour = "0" + time1_hour
                if int(time1_min) < 10:
                    time1_min = "0" + time1_min
                if int(time2_hour) < 10:
                    time2_hour = "0" + time2_hour
                if int(time2_min) < 10:
                    time2_min = "0" + time2_min

                self.mypetfeed.setfeedtime(time1_hour + ":" + time1_min, time2_hour + ":" + time2_min)

        except:
            pass
        finally:
            pass
