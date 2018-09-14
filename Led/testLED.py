import RPi.GPIO as GPIO
import time as t

PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

while True:
	GPIO.output(PIN, GPIO.HIGH)
	t.sleep(1)
	GPIO.output(PIN, GPIO.LOW)
	t.sleep(1)


	
