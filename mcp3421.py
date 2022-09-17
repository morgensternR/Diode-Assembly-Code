from machine import Pin, I2C
import time
class MCP3421:
    def __init__(self, i2c, addr=104):
        self.i2c = i2c
        self.addr = 104
        self.set_config(0x18)  # continuous and 16bit mode 0x18

    def set_config(self, register_value=0x18):
        
        data = bytes([register_value])
        #print('set_config', data)
        self.i2c.writeto(self.addr, data)
        #return data

    def read_adc(self):

        global i2c
        data = bytearray(2)
        self.i2c.readfrom_into(self.addr, data)
        result = int.from_bytes(data[:2],'big')
        if result & (1<<15):
            result = result - (1<<16)
        result = result * 2.048 / (1<<15)
        #print(data)
        return result
        
        return result



