import RPi.GPIO as GPIO
import time
pin=22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
time.sleep(3)
GPIO.output(pin, GPIO.LOW)
GPIO.cleanup()
