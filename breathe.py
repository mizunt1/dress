import RPi.GPIO as GPIO
import time

def glow_up(pin_list):
    for dc in range(0, 101, 5):
        for pin in pin_list:
            pin.ChangeDutyCycle(dc)
        time.sleep(0.1)
    return pin_list

def glow_down(pins_list):
    for dc in range(100, -1, -5):
        for pin in pins_list:
            pin.ChangeDutyCycle(dc)
        time.sleep(0.1)
       
if __name__ == '__main__':
    while True:
        p = glow_up(p1,p2,p3)
        time.sleep(5)
        glow_down(p, LedPins)
    
