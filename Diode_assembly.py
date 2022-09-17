from machine import SoftI2C, Pin, UART, I2C
import mcp3421 as mcp
import time
import uart_sw
import ADS as ads

i2c_list = []
diode_list = []

#For boards 0-8
for i in range(8):
  i2c_list.append(SoftI2C(scl = Pin(2*i, Pin.PULL_UP), sda = Pin(2*i + 1, Pin.PULL_UP), freq=400000, timeout=50000))

diode_list_i2c = [mcp.MCP3421(item) for item in i2c_list]
uart_sw_40K = uart_sw.uart_pio(Pin(16), Pin(17, Pin.IN, Pin.PULL_UP))
uart_sw_4K = uart_sw.uart_pio(Pin(18), Pin(19, Pin.IN, Pin.PULL_UP), sm_num = 2)


diode8 = ads.ADC('UART', uart_sw_40K, 24)
diode9 = ads.ADC('UART', uart_sw_4K, 24)
UART_diode = [diode8, diode9]
for i in UART_diode:
    i.reset()
    time.sleep(0.1)
    i.set_10ua()
    i.start()


