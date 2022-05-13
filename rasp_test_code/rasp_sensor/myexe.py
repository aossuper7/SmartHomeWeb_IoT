from watersensor import myWater
from feedtime import feedTime
from mymqtt import mymqttworker
from soundsensor import mySound



if __name__=="__main__":
    try: 
        mmw = mymqttworker("mypet/#")
        mmw.working()
        mysound = mySound()
        mysound.start()
        
    except KeyboardInterrupt:
        pass
    finally:
        pass