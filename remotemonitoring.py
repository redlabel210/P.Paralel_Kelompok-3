import paramiko
import sys
#sys.stdout = open("laporan.txt", "w")
ip = "192.168.100.9"
uname = "linuxlite"
sandi ="1234"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname= ip,username= uname,password= sandi)
stdin,stdout,stderr=ssh_client.exec_command("python3 monitoring.py")
print(stdout.readlines()) 
#sys.stdout.close
