#!replx
from machine import Pin
import time

OUT_PIN = 2
IN_PIN  = 3

outp = Pin(OUT_PIN, Pin.OUT)
inp  = Pin(IN_PIN,  Pin.IN, Pin.PULL_DOWN)

def loopback_test(n=50, dt_ms=20):
    fail = 0
    for i in range(n):
        outp.value(i & 1); time.sleep_ms(dt_ms)
        if inp.value() != outp.value(): fail += 1
    print("LOOPBACK:", "PASS" if fail==0 else "FAIL", "fail=", fail, "/", n)

loopback_test()