from machine import Pin, ADC, PWM
import time
#Name: Andy Gu
#Video: https://drive.google.com/file/d/1-GUu-GCwL-Hh8FUvjMKWi4JaOCYRUCv9/view?

led = Pin(25, Pin.OUT)
time_unit = 200
def dot():
    led.on()
    time.sleep_ms(time_unit)
    led.off()
    time.sleep_ms(time_unit)

def dash():
    led.on()
    time.sleep_ms(time_unit * 3)
    led.off()
    time.sleep_ms(time_unit)

def btLetter():
    led.off()
    time.sleep_ms(time_unit * 2)

while(True):
    dot()
    dash()
    btLetter()
    dash()
    dot()
    btLetter()
    dash()
    dot()
    dot()
    btLetter()
    dash()
    dot()
    dash()
    dash()
    time.sleep_ms(time_unit * 10)
