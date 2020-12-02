import luas
def jeda():
    print("--------------------------------------------")
    pass
print("Tugas Akhir Pemrosesan Paralel")
jeda()
print("Selamat datang di program mencari luas, luas apa yang ingin anda cari ?")
print("1. Luas Segitiga")
print("2. Luas Lingkaran")
print("3. Luas Persegi")
opsi = int(input("Masukkan nomor dari fungsi yang anda jalankan : "))
if (opsi==1):
    luas.segitiga()
    pass
elif (opsi==2):
    luas.lingkaran()
    pass
elif (opsi==3):
    luas.persegi
    pass
else:
    print("Maaf tidak ada perintah yang tersedia dengan angka yang anda masukkan")
    pass