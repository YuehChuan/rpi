import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

PIN = 23
GPIO.setup(PIN, GPIO.OUT)
breath = GPIO.PWM(PIN, 50)
breath.start(0)

try:
	while True:
		for dc in range(0, 101, 5):
			breath.ChangeDutyCycle(dc)
			t.sleep(0.1)
		for dc in range(100, -1, -5):
			breath.ChangeDutyCycle(dc)
			t.sleep(0.1)
except KeyboardInterrupt:
	pass
breath.stop()
GPIO.cleanup()
