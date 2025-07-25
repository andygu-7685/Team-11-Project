from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(26))
roomtempadc = 32768  # theoretical value adc value at 25 degrees
roomtemp = 25

while True:
    adcvalue = adc.read_u16()

    temperature = roomtemp + (adcvalue - roomtempadc) / (-387)

    print(f"Temperature: {temperature}")
    sleep(1)