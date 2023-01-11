import serial
import serial.tools.list_ports                                             #for getting list of ports
import os

#import pySerial
#import serial.tools.ListPortInfo


ports = []

ports_list = serial.tools.list_ports.comports()

for p in ports_list:
    ports.append(p.device)                     

print(ports)
if len(ports)==0:
                         print("There is no ports connected...")
else:
                         pass
                     
                     
#info = serial.tools.ListPortInfo.hwid()
info = serial.tools.list_ports.grep("regexp", include_links=True)
#info1 = serial.tools.list_ports.name()
#print(info1)