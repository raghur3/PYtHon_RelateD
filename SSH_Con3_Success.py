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
    print("DONE")
    stdin, stdout, stderr = ssh_client.exec_command("/home/moschip/Sukanya_virtual/env/bin/python /home/moschip/Sukanya_virtual/env/bin/serial_rx_only.py")
    opt = stdout.readlines()
    opt = "".join(opt)
    print(opt)
    #for opt in stdout:
        #print(opt.strip())
ssh_client.close
print("="*40, "CONNECTION CLOSED......", "="*40)

