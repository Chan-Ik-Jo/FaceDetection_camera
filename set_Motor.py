from gpiozero import AngularServo as As
import numpy as np
from time import sleep
import math
from gpiozero.pins.pigpio import PiGPIOFactory


pigpio_factory = PiGPIOFactory()

servo1 = As(17,pin_factory=pigpio_factory)
servo2 = As(18,pin_factory=pigpio_factory)
servo1_now=0
servo2_now=0
servo1.angle=servo1_now
servo2.angle=servo2_now

def Motor1_x(angle):
    global servo1_now
    servo1_now+=angle
    if servo1_now>90:
        servo1_now=0
        servo1.angle=servo1_now
        return
    else:
        servo1.angle=servo1_now
        return
    
def Motor1_reverse_x(angle):
    global servo1_now
    servo1_now-=angle
    if servo1_now<-90:
        servo1_now=0
        servo1.angle=servo1_now
        return
    else: 
        servo1.angle=servo1_now
        return

def Motor2_y(angle):
    global servo2_now
    servo2_now+=angle
    if servo2_now>90:
        servo2_now=0
        servo2.angle=servo2_now
        return
    else:
        servo2.angle=servo2_now
        return

def Motor2_reverse_y(angle):
    global servo2_now
    servo2_now-=angle
    if servo2_now<-90:
        servo2_now=0
        servo2.angle=servo2_now
        return
    else:
        servo2.angle=servo2_now
        return