import luas
inputan = open("input.txt", "r")
dataraw = inputan.readlines()
bidang = int(dataraw[0])
nilai1 =int(dataraw[1])
nilai2 =int(dataraw[2])
# print(luasdicari)
# print(type(luas[0]))
if (bidang==1):
    luas.segitiga(nilai1,nilai2)
    pass
if (bidang==2):
    luas.persegi(nilai1)
    pass
if (bidang==3):
    luas.lingkaran(nilai1)
