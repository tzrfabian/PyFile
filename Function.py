import math

def find_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    
    return luas_persegi_panjang

luas_pj = find_luas_persegi_panjang(5,7)
print(luas_pj)

def find_luas_lingkaran(phi, rad):
    luas_lingkaran = phi*pow(rad,2)
    
    return luas_lingkaran

luas_lkr = find_luas_lingkaran(math.pi, 7)
print(luas_lkr)
