import math
def jeda():
    print("--------------------------------------------")
    pass
def bulat(nilai):
    out = round(nilai,2)
    return out
    pass
def segitiga():
    alas=int(input("Masukkan alas : "))
    tinggi=int(input("Masukkan Tinggi :"))
    luas=alas*tinggi/2
    luas =bulat(luas)
    print("luas dari segitiga adalah ",luas,"cm^2")
    jeda()
# luas_segitiga()
def persegi():
    sisi = int(input("Masukkan panjang sisi :"))
    hasil = sisi*sisi
    hasil = bulat(hasil)
    print("luas persegi tersebut adalah ",hasil,"cm^2")
    jeda()
    pass
# luas_persegi()
def lingkaran():
    r = int(input("Masukkan jari jari lingkaran: "))
    luas = math.pi*r*r
    luas = bulat(luas)
    print("luas lingkaran adalah ",luas,"cm^2")
    jeda()
    pass




