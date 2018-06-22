import utime
from machine import Pin

led = Pin(15, Pin.OUT)
while True:
    led.value(0)
    utime.sleep_ms(500)
    led.value(1)
    utime.sleep_ms(500)

