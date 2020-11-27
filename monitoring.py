#!/usr/bin/env python
import psutil 
import os
# gives a single float value
print("cpu yang digunakan =", psutil.cpu_percent(interval= 1),"%")
print(psutil.virtual_memory())  # physical memory usage
print('ram yang digunakan:', psutil.virtual_memory()[2],"%")
print(psutil.net_io_counters())
rxtx=str(os.popen('ifconfig | grep MB').readlines())
print(rxtx)