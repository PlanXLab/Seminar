#!replx
from machine import Pin, PWM
import time

servo = PWM(Pin(1))    # Servo Motor
servo.freq(50)         # period = 1/50 = 0.02s = 20ms

def set_angle(angle):
    """
    angle   pulse width
    0       0.5ms
    90      1.5ms
    180     2.5ms
    """
    min_duty = 1638    # 0.5ms → 0.5ms/20ms = 0.025(2.5%), 65536 x 0.025 = 1638.375
    max_duty = 8192    # 2.5ms → 2.5ms/20ms = 0.125(12.5%), 65536 x 0.125 = 8191.875
    duty = int(min_duty + (max_duty - min_duty) * angle / 180)
    servo.duty_u16(duty)

for angle in (0, 90, 180, 90):
    set_angle(angle)
    time.sleep(1)
