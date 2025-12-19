#!replx
import network, socket
from machine import ADC, Pin
import time

SSID = "HBE_RSP"        # Your wifi ssid
PASSWORD = "hanback91!" # Your wifi password
SERVER_PORT = 5000      # Server Port

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Connecting to network...")
    time.sleep_ms(1000)

ip = wlan.ifconfig()[0]
print("Server IP:", ip)

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', SERVER_PORT))
sock.listen(1)

print("Server ready (VR / LED ON / LED OFF)")

adc = ADC(Pin(27))           # ADC1_VR
led = Pin("LED", Pin.OUT)    # Core LED

try:
    while True:
        conn, addr = sock.accept()
        cmd = conn.recv(64).decode().strip().upper()

        if cmd == "VR":
            value = adc.read_u16()
            resp = f"VR={value}"

        elif cmd == "LED ON":
            led.value(1)
            resp = "LED=ON"

        elif cmd == "LED OFF":
            led.value(0)
            resp = "LED=OFF"

        else:
            resp = "ERROR: UNKNOWN COMMAND"

        conn.send(resp + "\n")
        conn.close()
except KeyboardInterrupt:
    sock.close()
    print("Server stopped")