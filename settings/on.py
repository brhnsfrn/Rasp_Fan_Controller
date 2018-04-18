import RPi.GPIO as GPIO
import time
import os

def getCPUtemp():
    cTemp=os.popen('vcgencmd measure_temp').readline()
    return float(cTemp.replace("temp=","").replace("'C\n",""))

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(2,100)

while True:
    time.sleep(5)
    CPU_temp = getCPUtemp()

    if CPU_temp > 89 :
        p.start(100)
    elif CPU_temp > 79 :
        p.start(95)
    elif CPU_temp > 69 :
        p.start(90)
    elif CPU_temp > 59 :
        p.start(85)
    elif CPU_temp > 49 :
        p.start(80)
    elif CPU_temp > 39 :
        p.start(75)
    elif CPU_temp > 34 :
        p.start(70)
    elif CPU_temp > 30 :
        p.start(60)
    else :
        p.start(0)
    
GPIO.cleanup ()