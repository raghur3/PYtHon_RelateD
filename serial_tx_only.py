
import os
import sys
import serial
import io
import pymodbus
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient

import sys
import time
def Transfer():
    

    print("="*40, "Receiving Data", "="*40)
    dummy()
    #SerialObj.close()# Close the port
    
    
    print("closed")
    sys.exit()
    
    
    
    
def dummy():
                         import paramiko
                         import time
                         import os

                         devices = [
                         {
                         'ip_address' : '192.168.110.64',
                         'vendor' : 'broadcom',
                         'username' : 'moschip',
                         'password' : '1234'
                         }
                         
                         ]

                         ssh_client = paramiko.SSHClient()
                         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                         for device in devices:
                                                  ssh_client.connect(hostname=device['ip_address'],
                                                  username=device['username'],
                                                  password=device['password'],
                                                  
                                                  look_for_keys=False)
                                                  

                                                  print("success login to {}".format(device['ip_address']))
                         
                                                  print("="*40, "CONNECTION ESTABLISHED......", "="*40)
                         
                                                  stdin, stdout, stderr = ssh_client.exec_command("/home/moschip/Sukanya_virtual/env/bin/python /home/moschip/Sukanya_virtual/env/bin/serial_rx_only.py")
                                                  print("="*40, "transmit Data......", "="*40)
                                                  SerialObj = serial.Serial('COM5') # COMxx   format on Windows
                                                                           # ttyUSBx format on Linux

                                                  SerialObj.baudrate = 9600  # set Baud rate to 9600
                                                  SerialObj.bytesize = 8     # Number of data bits = 8
                                                  SerialObj.parity   ='N'    # No parity
                                                  SerialObj.stopbits = 1     # Number of Stop bits = 1

                                                  # time.sleep(3)
                                                  #f= open("guru123.txt","w+")
                                                  SerialObj.write(b'RK') #transmit 'A' (8bit) to micro/Arduino
                                                  #response = client.read_holding_registers(0x00,4,unit=1)
                                                  #print(response.getRegister(2))
                                                  #pymodbus.ReadRegistersRequestBase(0x7E201000)
                                                  #pymodbus.decode(0x7E201000)
                                                  #io.flush()
                                                  #c=io.readlines('-1')
                                                  #print(c)
                                                  #f1=f.write('A')
                                                  #content=f.read()
                                                  #print(content)
                                                  # print(stdin, stdout, stderr)
                                                  opt = stdout.readlines()
                                                  opt = "".join(opt)
                                                  print("Waiting for receive ")
                                                  print(opt)
                         #for opt in stdout:
                         #print(opt.strip())
                         ssh_client.close
                         print("="*40, "CONNECTION CLOSED......", "="*40)
                         

Transfer()




