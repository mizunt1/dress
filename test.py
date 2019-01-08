from breathe import glow_up, glow_down
from sensor import measurement
red_pins = [12, 8, 5]
red_on = False
blue_on = False
try:

    distance_is = measurement()
    
    if distance > 30:
        if red_on is False:
            red_objects = glow_up(red_pins)
            red_on = True
        if blue_on is True:
            # glow_down(blue_objects, blue_pins)
            print("blue off")
            blue_on = False
            
    else if distance > 10 and distance < 20:
        if red_on:
            pass
        else:
            red_objects = glow_up(red_pins)
            red_on = True
        if blue_on:
            pass
        else:
            # blue_objects = glow_up(blue_pins)
            print("blue on")
            blue_on = True
            
    elif distance < 30 :
        if red_on is True:
            glow_down(red_objects, red_pins)
            red_on = False
        if blue_on is False:
            # glow_up(blue_pins)
            blue_on = True
            print("blue on")
    time.sleep(1.5)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup() 

