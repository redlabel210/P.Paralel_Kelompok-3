
import paramiko
import socket
def pilihsshdankirim(node):
	node=int(node)
	if node==1:
		ip = "192.168.1.9"
		usrname = "mtaufik"
		passwd = "jamtangan"

	elif node==2:
		ip = "192.168.1.9"
		usrname = "user2"
		passwd = "pass2"
	else :
		ip = "192.168.1.9"
		usrname="dummy"
		passwd="pass2"
		
	coba_ssh = paramiko.SSHClient()
	coba_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		coba_ssh.connect(hostname=ip, username=usrname, password=passwd,timeout=3)
		coba_ftps = coba_ssh.open_sftp()
		print("berhasil tersambung")
		file="clientcomputing.py"
		coba_ftps.put(file,file)
		#coba_ftps.put("luas.py","luas.py")
		coba_ftps.put("input.txt", "input.txt")
		coba_ftps.close()
		cmd= "python3 clientcomputing.py"
		stdin,stdout,stderr= coba_ssh.exec_command(cmd)
		output=stdout.readlines()
		print(*output, sep ="\n")
		status = 'ONLINE'
	except(socket.gaierror,socket.timeout):
		print("node yang anda gunakan sedang tidak aktif")
		
	
