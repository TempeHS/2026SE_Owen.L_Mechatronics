from servo import Servo
from machine import Pin, PWM
import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

class Simple_Movement:      #basic movement functions
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

class Ultrasonic:               #ultrasonic sensor
    def __init__(self, range_a, range_b):
        self.__range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.__range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

    def Forward_dis(self):
        return int(self.__range_a.distance_mm) 

    def Side_dis(self):
        return int(self.__range_b.distance_mm)

class Combination(Simple_Movement, Ultrasonic):     #combining the movement functions and ultrasonic sensor functions        
    def __init__(self, forward, side, state):
        self.__forward = int(Ultrasonic.Forward_dis(self))
        self.__side = int(Ultrasonic.Side_dis(self))

    def set_idle(self):
        print ("IDLE")
        Simple_Movement.Idle
        self.__state = "idle"

    def forward(self):
        print ("FORWARD")
        Simple_Movement.Move_forward
        self.__state = "forward"

    def turn_right(self):
        print ("RIGHT")
        Simple_Movement.R_Turn
        self.__state = "right"

    def turn_left(self):
        print ("LEFT")
        Simple_Movement.L_Turn
        self.__state = "left"

    def back(self):
        print ("REVERSE")
        Simple_Movement.Backward
        self.__state = "backwards"

    def united(self):
        print("manchester")
        forward = self.Forward_dis()
        side_distance = self.Side_dis()
        print("Forward distance:", forward_distance)
        print("Side distance:", side_distance)
        if forward_distance < 100:
            if side_distance < 100:
                self.turn_left()
            else:
                self.turn_right()
        else:
            self.forward()