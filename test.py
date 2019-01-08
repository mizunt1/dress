from breathe import glow_up, glow_down
import RPi.GPIO as GPIO   
from sensor import measurement
import time
red_pins = [12, 8, 5]
red_on = False
blue_on = False
GPIO.setmode(GPIO.BOARD)
# Numbers pins by physical location
for red_pin in red_pins:
    GPIO.setup(red_pin, GPIO.OUT)

p1 = GPIO.PWM(red_pins[0], 1000)
p2 = GPIO.PWM(red_pins[1], 1000)
p3 = GPIO.PWM(red_pins[2], 1000)
p1.start(0)
p2.start(0)
p3.start(0)

try:
    while True:
        distance = measurement()
        print(distance)
        if distance > 30:
            if red_on is False:
                red_objects = glow_up(p1,p2,p3)
                red_on = True
                print("dis more 30 red on")
            if blue_on is True:
                # glow_down(blue_objects, blue_pins)
                print("blue off")
                blue_on = False
            
        elif distance > 20 and distance < 30:
            if red_on:
                pass
            else:
                red_objects = glow_up(p1,p2,p3)
                red_on = True
                print("dis middle red on")
            if blue_on:
                pass
            else:
                # blue_objects = glow_up(blue_pins)
                print("blue on")
                blue_on = True
            
        else:
            if red_on is True:
                glow_down(red_objects, red_pins)
                red_on = False
                print("diss less 30, red off")
            if blue_on is False:
                # glow_up(blue_pins)
                blue_on = True
                print("blue on")
    time.sleep(1.5)

except KeyboardInterrupt:
    print("Measurement stopped by User")

