import luas
import transferfile as ftp
def jeda():
    print("--------------------------------------------")
    pass
def pilihpc():
	print("pilih pc mana yang ingin dijalankan")
	print("1. PC1")
	print("2. PC2")
	node = input("masukkan disini :")
	return node
def mainPro():
	print("Selamat datang di program mencari luas dan keliling, pengoperasian apa yang ingin anda cari ?")
	print("1. Luas dan keliling Segitiga")
	print("2. Luas dan Keliling Persegi")
	print("3. Luas dan Keliling Lingkaran")
	print("4. Keluar ")
	opsi = int(input("Masukkan nomor dari fungsi yang anda jalankan : "))
	if (opsi==1):
		alas=input("masukkan panjang alas : ")
		tinggi=input("masukkan panjang tinggi segitiga: ")
		f=open("input.txt","w")
		f.write("1\n{}\n{}".format(alas,tinggi))
		f.close()
		node = int(pilihpc())
		if(node==3):
			ftp.pilihsshdankirim(1)
			ftp.pilihsshdankirim(2)
			
		ftp.pilihsshdankirim(node)
		lanjut()
		pass
	elif (opsi==2):
		sisi=input("masukkan panjang sisi: ")
		f=open("input.txt","w")
		f.write("2\n{}\n0".format(sisi))
		f.close()
		node = pilihpc()
		ftp.pilihsshdankirim(node)
		lanjut()

	elif (opsi==3):
		ruas=input("masukkan panjang jari jari: ")
		f=open("input.txt","w")
		f.write("3\n{}\n0".format(ruas))
		f.close()
		node = pilihpc()
		ftp.pilihsshdankirim(node)
		lanjut()
	elif (opsi==4):
		print('Terimakasih')
		
	else:
		print("Maaf tidak ada perintah yang tersedia dengan angka yang anda masukkan")

def lanjut():
	power = True
	while (power):
		jawaban =input("lanjut ? (y/n) :  ")
		if (jawaban=='y'):
			power = True
			mainPro()
			pass
		elif (jawaban=='n'):
			power = False
			pass
		else:
			print("input salah")
	print("Terimakasih")
mainPro()
jeda()