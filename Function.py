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

def greetings(name, message):
    return "Hello, " + name + '! ' + message

print(greetings("Ahmad", "Welcome to Momoa."))
print(greetings(message="Test", name="One Two"))

## Positional Only ##
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))
# print(penjumlahan(a=3, b=5)) # Kalo pake ini kena TypeError

## Keyword-Only ##
def salam(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(salam(pesan="Selamat pagi!",nama="Jack"))
# print(salam("Selamat sore!","Dicoding")) # Kalo pake ini kena TypeError

## Var-Positional (Variadic Positional Parameter) ##
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))
print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))

## Var-Keyword (Variadic Keyword Parameter) ##
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Ahmad", usia="17", pekerjaan="Python Programmer"))
print(cetak_info(nama="Ahmad", usia="17", pekerjaan="Python Programmer", tempat_lahir="Bandung", lulusan="ITB"))

def minimal(a, b):
    if a > b:
        hasil = print(b)
    elif a < b:
        hasil = print(a)
    else:
        hasil = print(a)
    return hasil

minimal(3,5)