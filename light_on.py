import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)  
print "LED on"
GPIO.output(3,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)

time.sleep(3)
print "LED off"
GPIO.output(3,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)