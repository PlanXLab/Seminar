#!replx
from machine import ADC, Pin
import time

ADC_PIN = 27         # ADC1_VR
adc = ADC(Pin(ADC_PIN))

LOW_MAX  = 15000     # LOW upper limit
HIGH_MIN = 50000     # HIGH lower limit

def classify(x):
    if x <= LOW_MAX: return "LOW"
    if x >= HIGH_MIN: return "HIGH"
    return "THRESHOLD"  # ambiguous section

while True:
    x = adc.read_u16()
    print(x, classify(x))
    time.sleep_ms(200)