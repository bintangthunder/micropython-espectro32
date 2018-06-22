from machine import Pin, PWM
# import time
import utime

pwm = PWM(Pin(15))

pwm.duty(896)
#time.sleep(10)
utime.sleep_ms(500)

pwm.duty(512)
# time.sleep(10)
utime.sleep_ms(500)

pwm.duty(0)
