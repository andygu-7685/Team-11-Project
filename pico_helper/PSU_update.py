"""
INSTRUCTIONS

Control your output voltage to be close to 0.8V. Your ripple should be at most 50mV after 30 seconds.

You are free to control these lines:
####
switchpin.freq(INSERTFREQUENCYHERE)
referenceadcvalue = INSERTREFERENCEADCVALUEHERE
referencepwmvalue = INSERTREFERENCEPWMVALUEHERE
changerate = INSERTCHANGERATE
printoutcount = -1000
####
and whichever pins you wish to choose, of course

For the reference values:
adc - what value do you expect when reading 0.8V?
pwm - what pwm is necessary to keep the voltage at 0.8V? (make another program to test this)

For frequency and changerate - what values gives you less than 50mV ripple?

changerate is a scalar, which determines how sensitive the power supply is to small changes. when changerate is ~ 1 (1 is pretty large), small fluctuations give large changes, and vice versa

printoutcount is just a buffer to allow the circuit to reach 0.8V before starting to measurethe max and min value. set it to a more negative value to allow for more time

I'll give full points if you can get under 50mV, but try to get under 50mV.
There is a prize for whoever has the lowest ripple and accurate voltage after 30 seconds.



"""

from machine import Pin, PWM, ADC
from time import sleep, sleep_ms
import time

adcpin = ADC(Pin(26))
switchpin = PWM(Pin(15))

####
switchpin.freq(1120)
referenceadcvalue = 16138
referencepwmvalue = int(65535/2)
changerate = 1
printoutcount = -1000
####

max = 0
min = 65535
currenttime = 0

while True:
    adcvalue = adcpin.read_u16()
    adcdiff = referenceadcvalue - adcvalue
    sleep_ms(1)
    switchpin.duty_u16(referencepwmvalue - int(adcdiff))
    sleep_ms(1)
    printoutcount += 1
    if printoutcount > 10:
        printoutcount = 0
        if adcvalue > max:
            max = adcvalue
        if adcvalue < min:
            min = adcvalue
        if currenttime == 0:
            currenttime = time.time()
        print(
            "current V: "
            + "{:.3f}".format(adcvalue * 3.3 / 65535)
            + " max V: "
            + "{:.3f}".format(max * 3.3 / 65535)
            + " min V: "
            + "{:.3f}".format(min * 3.3 / 65535)
            + " max ripple mV: "
            + "{:.3f}".format((max - min) * 3.3 * 1000 / 65535)
            + " time: "
            + str(time.time() - currenttime)
        )






#current V: 0.763 max V: 0.774 min V: 0.745 max ripple mV: 29.810 time: 36
