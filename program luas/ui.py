import luas
def jeda():
    print("--------------------------------------------")
    pass
def lanjut():
    status = 1
    while (status==1):
        jawaban =input("lanjut ? (y/n) :  ")
        if (jawaban=='y'):
            power = True
            status =-1
            pass
        elif (jawaban=='n'):
            power = False;
            status =-1
            pass
        else:
            print("input salah")
print("Tugas Akhir Pemrosesan Paralel")
jeda()
power = True
while (power==True):
    print("Selamat datang di program mencari luas, luas apa yang ingin anda cari ?")
    print("1. Luas Segitiga")
    print("2. Luas Lingkaran")
    print("3. Luas Persegi")
    print("4. Keluar ")
    opsi = int(input("Masukkan nomor dari fungsi yang anda jalankan : "))
    if (opsi==1):
        luas.segitiga()
        lanjut()
        pass
    elif (opsi==2):
        luas.lingkaran()
        lanjut()
        pass
    elif (opsi==3):
        luas.persegi
        lanjut()
        pass
    elif (opsi==4):
        power = False
        pass
    else:
        print("Maaf tidak ada perintah yang tersedia dengan angka yang anda masukkan")
        pass