import RPi.GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG,True)
time.sleep(0.0001)
GPIO.output(TRIG, False)


while GPIO.input(ECHO) == False:
	start = time.time()

while GPIO.input(ECHO) == True:
	end = time.time ()

sig_time = end-start 

#cm

distance = sig_time / 0.000058


print('Distance:: {} centimeters' .formatdistance())


GPIO.cleanup()
