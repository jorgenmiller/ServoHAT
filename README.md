# ServoHAT

See my pi's [setup](https://github.com/jorgenmiller/Raspberry-Pi-Setup.git).  
Make sure that I2C and SPI is enabled on your pi using `sudo raspi-config`.

## Hardware

I use [Adafruit's 16-Channel PWM Servo HAT for Raspberry Pi](https://www.adafruit.com/product/2327).  

### Servos

| Continuous | 180° Rotation |  
| --- | --- |  
| [Micro](https://www.adafruit.com/product/2442) | [Micro](https://www.adafruit.com/product/169) |   
| [Standard](https://www.adafruit.com/product/154) | [Standard](https://www.adafruit.com/product/155) |    

To make the continuous servos stop at 0 throttle, adjust the screw on the servo. The servos are digital, so they must be adjusted to your servo controller's signal.  

Continuous servos can work using the code for 180° servos. Continuous servos, as well as having no physical internal blocks, work by having the encoder always read as 90°, so setting the angle to 0° or 180° will rotate the servo until it is told to turn to 90° again. Note that they can no longer know their actual angle. Originally, continuous servos were made by hobbyists who found this trick, but now they are produced as separate products. There are also [continuous rotation servos with encoders](https://www.adafruit.com/product/3614), with the abilities of both types of servo.

## Install Libraries

The Adafruit CircuitPython Library Bundle ensures that all dependencies are available, but requires the CircuitPythonn Build Tools for itself.
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

To use the library, the programs must be run with python3

```python
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, address=65)

kit.continuous_servo[0].throttle = 1 #1 to -1
kit.servo[0].angle = 180 #0 to 180
```

[ServoKit docs](https://circuitpython.readthedocs.io/projects/servokit/en/latest/#)
