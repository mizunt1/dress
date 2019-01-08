import RPi.GPIO as GPIO
import time
LedPin = 12
GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output


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


def glow_up(pin):
    p = GPIO.PWM(pin, 1000)
    p.start(0)
    for dc in range(0, 101,5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    return p

def glow_down(p, pin):
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    p.stop()
    GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

p = glow_up(LedPin)
glow_down(p, LedPin)
    
