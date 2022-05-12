import mymqtt
from led import LED
import time
import RPi.GPIO as GPIO
import servo

# myled = LED()
        
if __name__=="__main__":
    try:
        mqtt = mymqtt.Mqttworker()
        mqtt.mymqtt_connect()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        # myled.clean()
        GPIO.cleanup()