import RPi.GPTO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, HIGH)
time.sleep(5)
GPIO.output(18, LOW)
GPIO.cleanup()

