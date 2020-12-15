import math
def jeda():
	print("--------------------------------------------")
	pass
def bulat(nilai):
	out = round(nilai,2)
	return out
	pass
def segitiga(alas,tinggi):
	luas=alas*tinggi/2
	luas =bulat(luas)
	keliling = alas+alas+alas
	keliling = bulat(keliling)
	print("luas dari segitiga adalah ",luas,"cm^2")
	print ("keliling luas sgitiga tersebut adalah ", keliling,"cm")
	jeda()
# luas_keliling_persegi()
def persegi(sisi):
	hasil = sisi*sisi
	hasil = bulat(hasil)
	keliling = 4*sisi
	keliling = bulat(keliling)
	print("luas persegi tersebut adalah ",hasil,"cm^2")
	print ("keliling persegi adalah ", keliling,"cm")
	jeda()
	pass
# luas_keliling_lingkaran()
def lingkaran(r):
	luas = math.pi*r*r
	luas = bulat(luas)
	keliling= math.pi*2*r*r
	keliling = bulat(keliling)
	print("luas lingkaran adalah ",luas,"cm^2")
	print("keliling lingkaran adalah ",keliling, "cm")
	jeda()
	pass




