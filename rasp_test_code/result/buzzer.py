import RPi.GPIO as g


class Buzzer:
    def __init__(self):
        self.buzzerPin = 16
        g.setmode(g.BCM)
        g.setup(self.buzzerPin, g.OUT)
        self.pwm = g.PWM(self.buzzerPin, 262)

    def buzzerOn(self):
        self.pwm.start(50)

    def buzzerOff(self):
        self.pwm.stop()