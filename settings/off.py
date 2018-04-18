import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(2,100)

while True:
    p.start(0)

GPIO.cleanup ()