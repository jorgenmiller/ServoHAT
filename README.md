# ServoHAT
See my pi's [setup](https://github.com/jorgenmiller/Raspberry-Pi-Setup.git).  
Make sure that i2c is enabled on your pi.

## Hardware
I use [Adafruit's 16-Channel PWM Servo HAT for Raspberry Pi](https://www.adafruit.com/product/2327).  
I use continuous rotation servos, [normal](https://www.adafruit.com/product/154) and [micro](https://www.adafruit.com/product/2442).  

## Install Library
The Adafruit CircuitPython Library Bundle makes sure that all dependencies are available.
```
pip install circuitpython-build-tools
pip3 install adafruit-circuitpython-lis3dh
pip3 install adafruit-circuitpython-servokit
```

## i2c Adress
The board will be set as i2c device 0x40, but you can change it by soldering the i2c address connections on the board. Using multiple HATs on the same pi will require this.
```
sudo i2cdetect -y 1
```
An address of 0x40 is 64, 1x41 is 65 and so on.

## Python3 Usage

[ServoKit docs](https://circuitpython.readthedocs.io/projects/servokit/en/latest/#)
