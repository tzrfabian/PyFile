# x = 'True'
# print(type(x))

## MULTI LINE STRING ##
# multi_line = """Halo sobat!
# Nama ku Sun Go Kong.
# Dari Goa kera.
# """
# print(multi_line[0],multi_line[1])
# print(multi_line[5:])

## Formatted String ##
# nama = "Joko Tingkir"
# print(f"Hello, nama saya {nama}")

## %-formatting ##
# nama = "Joko Tingkir"
# print("Nama saya %s" % (nama))

## str.format() ##
# nama = "Joko Tingkir"
# print("Halo, Nama saya {}".format(nama))

## Data type List ##
# x = [1, 2.2, 'Strong', True]
# x[2] = 'String' #Mutable (dapat diubah)
# print(x[1], x[2])

## Contoh Indexing ##
# x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

# print(x[0])
# print(x[2])
# print(x[-1]) # diambil dari paling belakang
# print(x[-4])

## Contoh Konsep Slicing ##
# x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
## contoh "sequence[start:stop:step]"
# print(x[0:6:2]) 
# print(x[1:])
# print(x[:3])

## Tipe Data Tuple ##
## Tipe Data tuple bersifat immutable
# x = (1, "Dicoding", 1+3j)
# print(type(x))
# print(x[0:3])

## Variable Set ##
# x = {1,2,7,2,3,13,3}
# print(x)
# print(type(x))

## Set Union & Intersection ##
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7,8}

# union = set1.union(set2) ## Union sama dengan operasi gabungan
# print('Contoh Union: ', union)

# intersection = set1.intersection(set2) ## Intersection sama dengan operasi irisan
# print('Contoh Intersection: ', intersection)

## Tipe Data Dictionary
x = { 'name': 'Joko Tingkir', 'age': 35, 'isMarried': False }
# x['name'] = "Jaka Sembung" ## untuk mengubah data pada dictionary
# x['Job'] = "Pendekar" ## untuk menambahkan data pada dictionary
print (x['name'])
# del x['Job'] ## 'del' untuk menghapus data pada dictionary
print(x)
print(type(x))