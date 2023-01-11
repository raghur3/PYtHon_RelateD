import platform
import psutil
import pytest
import sys
 #!/usr/bin/env python3.11  Line 1
      # -*- coding: utf-8 -*- Line 2
      #----------------------------------------------------------------------------
      # Created By  : Ramakrishna...
      # Created Date: 22/11/2022 ..etc
      # version ='3.11'
      # ---------------------------------------------------------------------------
def test_platform_spec():
                         my_system = platform.uname()

                         print(f"System: {my_system.system}")
                         print(f"Node Name: {my_system.node}")
                         print(f"Release: {my_system.release}")
                         print(f"Version: {my_system.version}")
                         print(f"Machine: {my_system.machine}")
                         print(f"Processor: {my_system.processor}")
                         print(platform.architecture(executable=sys.executable, bits='', linkage=''))

                         print("=======================================")
                         plat_os = platform.platform()
                         print(plat_os)

                         # print CPU information
                         print("="*40, "CPU Info", "="*40)
                         # number of cores
                         print("Physical cores:", psutil.cpu_count(logical=False))
                         print("Total cores:", psutil.cpu_count(logical=True))


                         # CPU frequencies
                         cpufreq = psutil.cpu_freq()
                         print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                         print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                         print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

                         print("="*40, "RAM Info..", "="*40)
                         #Total RAM
                         print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
                         #Available RAM
                         print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
                         #Used RAM
                         print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
                         #RAM usage
                         print(f"RAM usage: {psutil.virtual_memory().percent}%")

test_platform_spec()
'''import dummylog
dl = dummylog.DummyLog()
dl.logger.info('Log File is Created Successfully')'''

