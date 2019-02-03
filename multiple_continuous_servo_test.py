import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, address=65) #i2c address 1x41

servos = [0, 4] #channels of servos
throttle = .2

try:
    while True:
        kit.continuous_servo[servos[0]].throttle = throttle #1st forward
        time.sleep(.5)
        kit.continuous_servo[servos[1]].throttle = throttle #2nd forward
        time.sleep(.5)
        kit.continuous_servo[servos[0]].throttle = -1 * throttle #1st backward
        time.sleep(.5)
        kit.continuous_servo[servos[1]].throttle = -1 * throttle #2nd backward
        time.sleep(.5)

finally:
    for servo in servos: #stop all servo channels
        kit.continuous_servo[servo].throttle = 0
