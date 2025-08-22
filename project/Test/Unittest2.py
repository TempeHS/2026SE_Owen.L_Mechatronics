from Movement import Ultrasonic 
ultra = Ultrasonic(range_a=[0, 0, 0, 0], range_b=[1, 0, 0, 0])

print("Forward distance:", ultra.Forward_dis(), "mm")
print("Side distance:", ultra.Side_dis(), "mm")