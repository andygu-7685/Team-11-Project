from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(26))

while True:
    adcvalue = adc.read_u16()
    print(f"{adcvalue}")
    sleep(1)