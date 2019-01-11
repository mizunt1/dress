from breathe import glow_up, glow_down
import RPi.GPIO as GPIO   
from sensor import measurement
import time
red_pins_num = [12, 8, 5]
blue_pins_num =  [29, 22] # 22, 33
red_on = False
blue_on = False
GPIO.setmode(GPIO.BOARD)
# Numbers pins by physical location
for red_pin in red_pins_num:
    GPIO.setup(red_pin, GPIO.OUT)

for blue_pin in blue_pins_num:
    GPIO.setup(blue_pin, GPIO.OUT)

red_pins = []
for red_pin in red_pins_num:
    red_pin = GPIO.PWM(red_pin, 1000)
    red_pins.append(red_pin)

blue_pins = []
for blue_pin in blue_pins_num:
    blue_pin = GPIO.PWM(blue_pin, 1000)
    blue_pins.append(blue_pin)

for pin in red_pins:
    pin.start(0)

for pin in blue_pins:
    pin.start(0)

try:
    while True:
        distance = measurement()
        print(distance)
        if distance > 30:
            if red_on is False:
                red_objects = glow_up(red_pins)
                red_on = True
                print("dis more 30 red on")
            if blue_on is True:
                glow_down(blue_pins)
                print("blue off")
                blue_on = False
            
        elif distance > 10 and distance < 30:
            if red_on:
                pass
            else:
                red_objects = glow_up(red_pins)
                red_on = True
                print("dis middle red on")
            if blue_on:
                pass
            else:
                blue_objects = glow_up(blue_pins)
                print("blue on")
                blue_on = True
            
        else:
            if red_on is True:
                glow_down(red_pins)
                red_on = False
                print("diss less 30, red off")
            if blue_on is False:
                glow_up(blue_pins)
                blue_on = True
                print("blue on")
    time.sleep(1.5)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    for pin in red_pins:
        pin.stop()
    for pin in blue_pins:
        pin.stop()
    GPIO.cleanup()
