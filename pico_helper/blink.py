from machine import Pin, ADC


# Example:
# pin0 = Pin(0, Pin.OUT)
# pin1 = Pin(1, Pin.IN)
# pwm2 = PWM(Pin(2, Pin.OUT))

# pwm2.duty_u16(int(65535 / 2))
# pwm2.freq(1000)

# led = Pin(25, Pin.OUT)
# led.on()

# time.sleep_ms(100)


adc = ADC(Pin(26))
adcvalue = adc.read_u16()

RAt0 = 79282.25

temperature = (10000 * adcvalue)/(235 * (adcvalue - 3.3 * 65535)) + (RAt0/235) - 273.15


#Perform some calculations to convert adcvalue to temperature
print(f"temp value: {temperature}")

#MicroPico: Connect