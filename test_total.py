#!replx
from machine import Pin, ADC
import time, math

OUT_PIN, IN_PIN = 2, 3
ADC_PIN = 27

LOW_MAX, HIGH_MIN = 15000, 50000          # Threshold Judgment Criteria
ADC_STD_MAX = 1200                        # Stability (Noise) Tolerance (Example)
REPEAT = 100

outp = Pin(OUT_PIN, Pin.OUT)
inp  = Pin(IN_PIN,  Pin.IN, Pin.PULL_DOWN)
adc  = ADC(Pin(ADC_PIN))

def mean(xs): return sum(xs)/len(xs)
def std(xs):
    m = mean(xs); return math.sqrt(sum((x-m)*(x-m) for x in xs)/len(xs))

def qa_loopback(n=REPEAT):
    fail = 0
    for i in range(n):
        v = i & 1
        outp.value(v); time.sleep_ms(5)
        if inp.value() != v: fail += 1
    return fail

def qa_threshold_and_noise(samples=80):
    xs = [adc.read_u16() for _ in range(samples)]
    s  = std(xs)
    x  = xs[-1]
    cls = "LOW" if x <= LOW_MAX else ("HIGH" if x >= HIGH_MIN else "THRESHOLD")
    return cls, s, x

def run_qa():
    lb_fail = qa_loopback()
    cls, s, x = qa_threshold_and_noise()

    v_lb  = (lb_fail == 0)
    v_thr = (cls != "THRESHOLD")           # If ambiguous, FAIL (Quality Standard)
    v_stb = (s <= ADC_STD_MAX)

    print("QA_LOOPBACK:", "PASS" if v_lb else "FAIL", "lb_fail=", lb_fail)
    print("QA_THRESHOLD:", "PASS" if v_thr else "FAIL", "adc=", x, "class=", cls)
    print("QA_STABILITY:", "PASS" if v_stb else "FAIL", "std=", int(s))

    overall = v_lb and v_thr and v_stb
    print("QA_OVERALL:", "PASS" if overall else "FAIL")

run_qa()
