#!replx
from machine import ADC, Pin
import time

adc = ADC(Pin(27))              # ADC1_VR
while True:
    v = adc.read_u16()          # 0~65535
    '''
    ADCs do not operate in the ideal 0-65535 range, 
    but in reality they operate with some offset and rail margin.
    '''
    print(v)                    # Ideal range: 0 to 65535, Actual range: 2xx to 64xxx
    time.sleep_ms(200)
