# ServoHAT

See my pi's [setup](https://github.com/jorgenmiller/Raspberry-Pi-Setup.git).  
Make sure that I2C and SPI is enabled on your pi using `sudo raspi-config`.

## Hardware

I use [Adafruit's 16-Channel PWM Servo HAT for Raspberry Pi](https://www.adafruit.com/product/2327).  

| Continuous | Standard |  
| --- | --- |  
| [Micro](https://www.adafruit.com/product/2442) | [Micro](https://www.adafruit.com/product/169) |   
| [Standard](https://www.adafruit.com/product/154) | [Standard](https://www.adafruit.com/product/155) |    

To make the continuous servos stop at 0 throttle, adjust the screw on the servo.

## Install Library

The Adafruit CircuitPython Library Bundle makes sure that all dependencies are available.
```
pip install circuitpython-build-tools
pip3 install adafruit-circuitpython-lis3dh
pip3 install adafruit-circuitpython-servokit
```

## I2C Address

The board will be set as i2c device 0x40, but you can change it by soldering the i2c address connections on the board. Using multiple HATs on the same pi will require this to differentiate them.
```
sudo i2cdetect -y 1
```
An address of 0x40 is 64, 1x41 is 65 and so on.

## Python3 Usage

```python
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=65)

kit.continuous_servo[0].throttle = 1 #1 to -1
kit.servo[0].angle = 180 #0 to 180
```

[ServoKit docs](https://circuitpython.readthedocs.io/projects/servokit/en/latest/#)
