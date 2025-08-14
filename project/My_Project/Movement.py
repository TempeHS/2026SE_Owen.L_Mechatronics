from servo import Servo
from machine import PWM
import time
import PiicoDev_Ultrasonic

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

class Ultrasonic:               #ultrasonic_sensor
    def __init__ (self, range_a, range_b):
        self.__range_a = range_a
        self.__range_b = range_b 

    def Distance(self):
        self.__range_a.distance_mm (id=[0, 0, 0, 0])
        self.__range_b.distance_mm (id=[1, 0, 0, 0])

    def Forward_dis(self):
        return int(self.__range_a.distance_mm) 

    def Side_dis(self):
        return int(self.__range_b.distance_mm)

class Combination:             
    def __init__(self, foward, side, state):
        self.__foward = foward
        self.__side = side
        self.__state = "sumtingwong"

    def set_idle(self):
        Simple_Movement.Idle

    def foward(self):
        Simple_Movement.Move_forward


    def turn_right(self):
        Simple_Movement.R_Turn


    def turn_left(self):
        Simple_Movement.L_Turn

    def back(self):
        Simple_Movement.Backward


