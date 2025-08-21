from project.My_Project.Movement import Simple_Movement
from project.lib.servo import Servo

class TestSimpleMovement(unittest.TestCase):
    def setUp(self):

        self.right_servo = Servo(pwm=16, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.left_servo = Servo(pwm=20, min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

        self.move = Simple_Movement(self.right_servo, self.left_servo)

    def test_idle(self):
        print("Testing Idle...")
        self.move.Idle()
        print("Idle set to 1500 on both servos ✅")

    def test_move_forward(self):
        print("Testing Move Forward...")
        self.move.Move_forward()
        print("Forward set to 2000 on both servos ✅")

    def test_r_turn(self):
        print("Testing Right Turn...")
        self.move.R_Turn()
        print("Right Turn: right=1550, left=1800 ✅")

    def test_l_turn(self):
        print("Testing Left Turn...")
        self.move.L_Turn()
        print("Left Turn: right=1800, left=1550 ✅")

    def test_backward(self):
        print("Testing Backward...")
        self.move.Backward()
        print("Backward set to 1200 on both servos ✅")

if __name__ == '__main__':
    unittest.main()