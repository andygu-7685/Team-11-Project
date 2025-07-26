from machine import Pin, ADC
import time            

ldr = ADC(Pin(27))  # Initialize an ADC object for pin 27

def LDRRead():
    ldr_value = ldr.read_u16()  # Read the LDR value and convert it to a 16-bit unsigned integer
    time.sleep(2)  
    return ldr_value