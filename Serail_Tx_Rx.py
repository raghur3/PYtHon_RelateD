import serial

import time
def Transfer():
        
    SerialObj = serial.Serial('COM5') # COMxx   format on Windows
                                       # ttyUSBx format on Linux

    SerialObj.baudrate = 9600  # set Baud rate to 9600
    SerialObj.bytesize = 8     # Number of data bits = 8
    SerialObj.parity   ='N'    # No parity
    SerialObj.stopbits = 1     # Number of Stop bits = 1

    time.sleep(3)

    SerialObj.write(b'A')      #transmit 'A' (8bit) to micro/Arduino
    print("done")
    #SerialObj.close()# Close the port
    
    print("="*40, "Calling reciving function", "="*40)
    reciving()
    print("closed")


import serial
from time import sleep
def reciving():
    ser = serial.Serial('/dev/ttyS0', 9600)

    while True:
        received_data = ser.read()
        sleep(0.03)
        data_left = ser.inWaiting()
        received_data += ser.read(data_left)
        print(received_data)
        ser.write(received_data)
        
print("="*40, "Calling transfer function", "="*40)
Transfer()