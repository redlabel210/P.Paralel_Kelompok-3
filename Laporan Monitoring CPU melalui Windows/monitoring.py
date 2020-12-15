#!/usr/bin/env python
import psutil 
import subprocess
import os
# gives a single float value
print("cpu yang digunakan =", psutil.cpu_percent(interval =1), "%")
#print(psutil.virtual_memory())  # physical memory usage
print('ram yang digunakan:', psutil.virtual_memory().percent,"%")
print('ram yang tersedia : ',  psutil.virtual_memory().available * 100 /psutil.virtual_memory().total,'%')
print("TX =",psutil.net_io_counters().bytes_sent/1024,"KB")
print("RX =",psutil.net_io_counters().bytes_recv/1024,"KB")
print(rx)
print (tx)

