import RPi.GPIO as GPIO
import time
LedPin = 12
LedPins = [12, 8, 5] 
# pin numbers, not gpio numbers
GPIO.setmode(GPIO.BOARD)
# Numbers pins by physical location
for LedPin in LedPins:
    GPIO.setup(LedPin, GPIO.OUT)



GPIO.output(LedPin, GPIO.LOW)  # Set pin to low(0V)

# p = GPIO.PWM(LedPin, 1000)     # set Frequece to 1KHz
# p.start(0)                     # Start PWM output, Duty Cycle = 0try:
# try:
#     while True:
#         for dc in range(0, 101, 5):
#             p.ChangeDutyCycle(dc)
#             time.sleep(0.05)
#         time.sleep(1)
#         for dc in range(100, -1, -5):
#             p.ChangeDutyCycle(dc)
#             time.sleep(0.05)
#         time.sleep(1)
# except KeyboardInterrupt:
#     p.stop()
#     GPIO.output(LedPin, GPIO.HIGH)    # turn off all leds
#     GPIO.cleanup()
pins = LedPins
p1 = GPIO.PWM(pins[0], 1000)
p2 = GPIO.PWM(pins[1], 1000)
p3 = GPIO.PWM(pins[2], 1000)
p1.start(0)
p2.start(0)
p3.start(0)

def glow_up(p1, p2, p3):
    for dc in range(0, 101, 5):
        p1.ChangeDutyCycle(dc)
        p2.ChangeDutyCycle(dc)
        p3.ChangeDutyCycle(dc)
        time.sleep(0.1)
    return [p1, p2, p3]

def glow_up_b(p1):
    for dc in range(0, 101, 5):
        p1.ChangeDutyCycle(dc)
        time.sleep(0.1)
    return p1

def glow_down(pins):
    for dc in range(100, -1, -5):
        pins[0].ChangeDutyCycle(dc)
        pins[1].ChangeDutyCycle(dc)
        pins[2].ChangeDutyCycle(dc)
        time.sleep(0.2)
    #pins[0].stop()
    #pins[1].stop()
    # pins[2].stop()
    #GPIO.output(pin[0], GPIO.HIGH)
    #GPIO.output(pin[1], GPIO.HIGH)
    #GPIO.output(pin[2], GPIO.HIGH)
    # GPIO.cleanup()

def glow_down_b(pins):
    for dc in range(100, -1, -5):
        pins.ChangeDutyCycle(dc)
        time.sleep(0.2)

if __name__ == '__main__':
    while True:
        p = glow_up(p1,p2,p3)
        time.sleep(5)
        glow_down(p, LedPins)
    
