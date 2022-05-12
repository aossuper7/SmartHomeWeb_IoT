from threading import Thread
import paho.mqtt.client as mqtt
from threading import Thread
from servo import Servo
from led import LED
import RPi.GPIO as GPIO
from servo import Servo


class Mqttworker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.led = LED()
        self.curtain = Servo()
        
    def mymqtt_connect(self):
        try:
            print("브로커 연결 시작하기")
            self.client.connect("192.168.219.102",1883,60)
            myThread = Thread(target=self.client.loop_forever)
            myThread.start()
        except KeyboardInterrupt:
            pass
        finally:
            print("종료")
    
    def on_connect(self,client, userdata, flags, rc):
        print("connect.."+str(rc))
        if rc==0:
            client.subscribe("iot/#")
        else:
            print("연결 실패..")
          
    def on_message(self,client, userdata, message):
        try:
            myvalue = message.payload.decode("utf-8")
            print(message.topic+"---"+myvalue)
            if myvalue == "led_on":
                self.led.led_on()
            elif myvalue == "led_off":
                self.led.led_off()
            elif myvalue == "servo_open":
                self.curtain.servo_open()
            elif myvalue == "servo_close":
                self.curtain.servo_close()
        except:
            pass
        finally:
            pass