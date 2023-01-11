import serial
SerialObj = serial.Serial('COM5') # COMxx   format on Windows
                                                                           # ttyUSBx format on Linux

SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1 # time.sleep(3)
                                                  #f= open("guru123.txt","w+")
SerialObj.write(b'A') #transmit 'A' (8bit) to micro/Arduino
print("Transmit")