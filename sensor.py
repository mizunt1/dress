#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def measurement():
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 40
    PIN_ECHO = 36
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(1)
    # print("Calculating distance")
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    # print("Distance:",distance,"cm")
    return distance
    # finally:
    #    GPIO.cleanup()

if __name__ == "__main__":
    try:
        while True:
            dist = measurement()
            time.sleep(0.25)
            print(distance)
            # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
