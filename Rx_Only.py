from time import sleep
from serial import Serial
ser=Serial('COM5', 9600)
#ser.write(0x12)
while True:
    
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially