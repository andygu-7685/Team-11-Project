from machine import Pin, ADC
import time  
import constants          

ldr = ADC(Pin(constants.LDR_PIN))  # Initialize an ADC object for pin 27

def LDRRead():
    """return brightness in percentage in two decimal places"""
    ldr_value = ldr.read_u16()  # Read the LDR value and convert it to a 16-bit unsigned integer
    ldr_value = (ldr_value / 65535) * 100    # convert to percentage
    ldr_value = round(ldr_value, 2) # round to 2 decimal places
    time.sleep(2)
    return ldr_value