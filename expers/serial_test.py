#!/bin/python3
from serial.tools import list_ports
import json
import asyncio
import sys
import serial
import time


class uartConfig:
    def __init__(self):
        self.uartDescription = None
        self.uartPort = None
        self.uartProduct = None
        self.baudrate = None
        self.ser = None
        self.fw_check = False

# write addition logic to clear JTAG/SWD state 
# In the firmware wrute an aditional character to exit the mode 
# In the firmware return in JSON for easier parsing 

def fw_check(uart_config: uartConfig):
    uart_config.ser.reset_input_buffer()
    uart_config.ser.write(b'@')

    start_time = time.time()
    while True:
        data = uart_config.ser.read(30)
        if data:
            #print(data.decode(errors="ignore"), end="")
            if b"ACK: silknode" in data:
                print(f"{fw_check.__name__}: silknode fw check pass")
                uart_config.fw_check = True
                break
                


def init_silknode():
    ports = list_ports.comports()
    config = uartConfig()
    
    for port in ports:
        if port.product == "silknode":
            config.uartPort = port.device
            config.uartProduct = port.product
            config.uartDescription = port.description
            config.baudrate = 115200
            print(f"{init_silknode.__name__}: silknode uart port at: {config.uartPort}")
            return config

    sys.exit(f"{init_silknode.__name__}: silknode uart port identification failed")

 
def uart_read(uart_config: uartConfig) -> str: 
    while True:
        data = uart_config.ser.read(32)
        if data:
            print(data.decode(errors="ignore"), end="")
            break
            # if b"ACK: silknode" in data:
            #     print(f"{fw_check.__name__}: silknode fw check pass")
            #     uart_config.fw_check = True
            #     break

#def uart_send(uart_config: uartConfig, cmd: str):
    


def swdScan(uart_config: uartConfig, cmd=b"s"): 
    uart_config.ser.reset_input_buffer()
    uart_config.ser.write(cmd)
    data = ""
    read_data = b""

    while True:
        data = uart_config.ser.read(64)
        if data:
            if b"Enter number of channels hooked up" in data or b"Enter a valid value" in data: 
                time.sleep(0.2)
                # print(data.decode(errors="ignore"), end="")
                uart_config.ser.write(b"16")
                break
    
    while True:
        bytes_available = uart_config.ser.in_waiting
        #print(f"{bytes_available} bytes_available")
        read_data += uart_config.ser.read(bytes_available)
        if b"No devices found. Please try again." in read_data: 
            print("Failed to initialize SWD port")
            break
        else:
            print("SUCESS") # fix success bug in fw and send reponse as JSON
            break

def init_uart(uart_config: uartConfig):
    ser = serial.Serial(
    port= uart_config.uartPort,  
    baudrate=uart_config.baudrate,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=2,          # non-blocking reads
    rtscts=False,
    dsrdtr=False
    )
    ser.setDTR(False)
    ser.setRTS(False)
    time.sleep(0.1)
    ser.setDTR(True)
    ser.setRTS(True)

    if ser.is_open == True:
        uart_config.ser = ser
        
    else:
        sys.exit(f"{init_uart.__name__}: serial port failed to connect")

if __name__ == '__main__':
	
    uart_config = init_silknode()
    init_uart(uart_config)
    fw_check(uart_config)
    swdScan(uart_config)