from machine import Pin, SoftI2C
import ssd1306
import constants
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(constants.OLEDSCL), sda=Pin(constants.OLEDSDA))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def OLEDShow(DisplayThis):
    """"display string in the parameter, the string can be multiline and will be displayed accordingly"""
    oled.fill(0)  # Clear display
    lines = DisplayThis.split('\n')
    for i, line in enumerate(lines):
        y = i * 10  # 10 pixels per line (adjust depending on font size)
        if y >= oled_height:
            break  # Avoid writing beyond screen
        oled.text(line, 0, y)
    oled.show()