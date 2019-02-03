import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16, address=65) #i2c address 1x41

kit.servo[0].angle = 180 #rotate to 180 degrees
time.sleep(1)
kit.servo[0].angle = 0 #rotate to 0 degrees
