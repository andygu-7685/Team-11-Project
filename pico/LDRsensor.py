from machine import Pin, ADC
import time  
import constants          

ldr = ADC(Pin(constants.LDR_PIN))  # Initialize an ADC object for pin 27
ADC_MAX = 65535  # 16-bit range from read_u16()

def LDRRead():
    raw_value = ldr.read_u16()
    # Convert to brightness percentage (inverse logic: higher light → lower resistance → higher voltage)
    brightness = (raw_value / ADC_MAX) * 100
    # Optional: round it to make it readable
    brightness = round(brightness, 1)
    return brightness
