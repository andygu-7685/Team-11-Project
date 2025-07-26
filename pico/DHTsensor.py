from machine import Pin
from time import sleep
import constants
import dht

sensor = dht.DHT11(Pin(constants.DHT_PIN))

def DHTRead(type):
  """"type = 1 if temperature in C,  
      type = 2 if temperature in F,  
      type = 3 if humidity"""
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
  except OSError as e:
    print('Failed to read sensor.')

  if(type == 1):
    return temp
  if(type == 2):
    return temp_f
  if(type == 3):
    return hum