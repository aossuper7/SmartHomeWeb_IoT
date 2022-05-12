import spidev
import time
import RPi.GPIO as GPIO

led_pin = 22
servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT, initial=GPIO.LOW)
pwm = GPIO.PWM(servo_pin,50)
pwm.start(3)  # 초기값 0으로 설정
# 딜레이 시간(센서 측정 간격)
delay = 2
# MCP3008 채널 중 센서에 연결한 채널 설정
pot_channel = 0
# SPI 인스턴스 spi통신을 하기 위한 객체 생성
spi = spidev.SpiDev()
# SPI 통신 시작하기
spi.open(0, 0)
# SPI 통신 속도 설정
spi.max_speed_hz = 100000
# 0 ~7 까지 8개의 채널에서 SPI 데이터 읽기
def readadc(adcnum):
    if adcnum < 0 or adcnum > 7:
        return -1
    # MCP3008과 통신하기 위한 패킷을 설정하는 작업
    r = spi.xfer2([1, 8+adcnum <<4, 0])
    # SPI를 통신을 통해서 받아온 센서 데이터는 8bit짜리 이고 이를 16bit로
    # 통합하는 과정
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        # readadc 함수로 pot_channel의 SPI 데이터를 읽기
        pot_value = readadc(pot_channel)
        if pot_value < 300 :
            GPIO.output(led_pin, GPIO.HIGH)
            pwm.ChangeDutyCycle(13)
        else :
            GPIO.output(led_pin, GPIO.LOW)
            pwm.ChangeDutyCycle(3)
        print("---------------------------")
        print("조도센서 값: %d" % pot_value) 
        time.sleep(delay)
except KeyboardInterrupt:
    pass
finally:
    pwm.ChangeDutyCycle(2.5)
    pwm.stop()
    GPIO.cleanup()