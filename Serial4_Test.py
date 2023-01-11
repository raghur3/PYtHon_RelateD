'''from busio import UART
serial = UART(14,15,baudrate=9600)
serial.write('Hello to Arduino')
answer = serial.readline()
print(answer)
serial.deinit()'''

from serial import Serial
with Serial('/dev/ttyS0', 9600) as serial:
  serial.send('Hello to Arduino')
  answer = serial.readline()
  print(answer)