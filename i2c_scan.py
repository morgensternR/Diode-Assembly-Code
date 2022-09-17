# Scanner i2c en MicroPython | MicroPython i2c scanner
# Renvoi l'adresse en decimal et hexa de chaque device connecte sur le bus i2c
# Return decimal and hexa adress of each i2c device
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

import machine
from machine import Pin
#i2c = machine.I2C(1, scl=machine.Pin(23), sda=machine.Pin(22))
i2c = machine.SoftI2C(Pin(0, Pin.PULL_UP), sda=Pin(1, Pin.PULL_UP), freq=400000, timeout=50000)


print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))