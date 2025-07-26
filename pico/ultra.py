from machine import Pin
import constants
import utime

trigger = Pin(constants.TRIG_PIN, Pin.OUT)
echo = Pin(constants.ECHO_PIN, Pin.IN)

def ultra():
    """return distance to the ultra sensor in cm"""
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)  # minimum 10 µs pulse
    trigger.low()

    timeout = 1000000  # 1 second timeout in µs
    start = utime.ticks_us()
    while echo.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), start) > timeout:
            print("Timeout: no echo start")
            return
    signaloff = utime.ticks_us()

    while echo.value() == 1:
        if utime.ticks_diff(utime.ticks_us(), signaloff) > timeout:
            print("Timeout: no echo end")
            return
    signalon = utime.ticks_us()

    timepassed = utime.ticks_diff(signalon, signaloff)
    distance = (timepassed * 0.0343) / 2.0
    return distance