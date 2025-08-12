from servo import Servo
from machine import PWM
import time

class Simple_Movement:
    def __init__ (self, right_Servo, left_Servo):
        self.__right_Servo = Servo(pwm=16, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.__left_Servo = Servo(pwm=20, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

    def Idle(self):
        self.__right_Servo.set_duty(1500)
        self.__left_Servo.set_duty(1500)

    def Move_forward(self):
        self.__right_Servo.set_duty(2000)
        self.__left_Servo.set_duty(2000)

    def R_Turn(self):
        self.__right_Servo.set_duty(1550)
        self.__left_Servo.set_duty(1800)

    def L_Turn(self):
        self.__right_Servo.set_duty(1800)
        self.__left_Servo.set_duty(1550)

    def Backward(self):
        self.__right_Servo.set_duty(1200)
        self.__left_Servo.set_duty(1200)

class Ultrasonic:
    def __init__ (self, range_a, range_b):
        self.__range_a = range_1 #check foward distance
        self.__range_b = range_2 #check side distance

    def Dis_Stop(self):
        self.__range_a.distance_mm (id=[0, 0, 0, 0])
        self.__range_b.distance_mm (id=[1, 0, 0, 0])

    def Dis_Move(self):

class Complicated_Movement:
    def __init__(self, ):