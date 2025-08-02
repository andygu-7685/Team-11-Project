from machine import ADC, Pin
import time

# Set up ADC on GPIO28 (which maps to ADC2)
ldr = ADC(Pin(28))

# Constants
ADC_MAX = 65535  # 16-bit range from read_u16()

def read_brightness():
    raw_value = ldr.read_u16()
    
    # Convert to brightness percentage (inverse logic: higher light → lower resistance → higher voltage)
    brightness = (raw_value / ADC_MAX) * 100

    # Optional: round it to make it readable
    brightness = round(brightness, 1)

    return brightness

# Main loop
while True:
    brightness = read_brightness()
    print("Brightness: {}%".format(brightness))
    time.sleep(0.5)