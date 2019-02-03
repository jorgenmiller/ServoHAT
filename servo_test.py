import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, address=65)

kit.servo[0].angle = 180
time.sleep(1)
kit.servo[0].angle = 0
