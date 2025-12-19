#!replx
from machine import Pin
import time

led = Pin("LED", Pin.OUT)
btn = Pin(16, Pin.IN, Pin.PULL_UP)

try:
    while True:
        led.value(not btn.value())
        time.sleep_ms(20)
except KeyboardInterrupt:
    led.value(0)
    print("Program stopped by user.")