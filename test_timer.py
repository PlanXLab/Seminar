#!replx
from machine import Timer, Pin

n = 0

def tick(t):
    global n

    n += 1
    led.toggle()

led = Pin("LED", Pin.OUT); 
timer = Timer(freq=2, mode=Timer.PERIODIC, callback=tick, hard=True)

input("Press <ENTER> and Quit")
timer.deinit()