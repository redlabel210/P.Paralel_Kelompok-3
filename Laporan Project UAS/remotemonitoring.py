import paramiko
ip = "192.168.1.10"
uname = "mtaufik"
sandi ="jamtangan"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname= ip,username= uname,password= sandi)
stdin,stdout,stderr=ssh_client.exec_command("ls")
#print(stdout.readlines()) 
sftp = ssh_client.open_sftp()
sftp.put("LUAS.py","3des.txt")

baca =stdout.readlines()
baca_soviet = stderr.readlines()

for i in baca_soviet:
	print (i)
for i in baca:
	print(i)