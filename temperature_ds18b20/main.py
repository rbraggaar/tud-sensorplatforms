"""
Note:
This sensor requires a 4.7k Ohm reistor between 3v3 and data.
"""
import time
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

# DS18B20 data line connected to pin P10
ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

while True:
    print(temp.read_temp_async())
    time.sleep(1)
    temp.start_convertion()
    time.sleep(1)
