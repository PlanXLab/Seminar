#!replx
from machine import I2C, Pin

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)

"""
0x27/0x3F : LCD1602 + PCF8574 I2C address
0x69 : MPU6050 I2C address
"""
addrs = i2c.scan()
print([hex(a) for a in addrs])