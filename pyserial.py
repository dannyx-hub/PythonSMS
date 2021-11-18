import time
import serial
from serial.serialutil import STOPBITS_ONE

#setup serial connection
ser = serial.Serial(
        port='COM1',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
        )
try:
    if ser.isOpen() == False:
        ser.open()
    else:
        ser.close()
    print(ser.isOpen())
except Exception as e:
    print(f"[!] Serial error: {e}")
