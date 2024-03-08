## Mengubah String UpperCase/LowerCase ##
# kata = 'kungkingkang'
# kata = kata.upper() #uppercase
# kata = kata.lower() #lowercase
# print(kata)

## rstrip() untuk menghapus whitespace pada sebelah kanan atau akhir string ##
# print("Halo Dunia   ".rstrip())

## lstrip() untuk menghapus whitespace pada sebelah kiri atau awal string ##
# print("           hellooow".lstrip())

## strip() untuk menghapus whitespace pada awal dan akhir string ##
# print("      hellooow      ".strip())
# kata = "WawiWawiOWIWOWawiWawi"
# print(kata.strip("Wawi"))

## Method startswith() bertujuan untuk menemukan suatu kata pada awal string, sedangkan endwith() untuk menemukan suatu kata pada akhir string.##
# print('Halo Dunia'.startswith('Halo'))
# print('Halo Dunia'.endswith('Dunia'))
## Method tersebut mengembalikan nilai true. ##

## Method join, untuk menggabungkan dan memisahkan string
# print(' '.join(['Jaka','Sembung', 'Bergolok!']))
# print(' bawa '.join(['Jaka','Golok']))

## Method split() untuk memisahkan string berdasarkan delimiter
# print('halo Dunia !'.split())

## Method replace() untuk menggantikan kata pada string ##
# kata = "Ayo makan Bebek Bakar di Warung Pak Somad!"
# print(kata.replace("Bebek","Ayam"))

## Method isupper() untuk mengecek apakah kata pada string huruf kapital semua, sedangkan islower() sebaliknya. ##
# kata1 = 'SAMBAL'
# kata2 = 'makan'
# kata3 = 'SaPi'
# print(kata1.isupper())
# print(kata2.islower())
# print(kata3.isupper())

## Method isalpha() untuk mengecek apakah dalam sebuah string berisi huruf alfabet ##
# kata = 'orpheus'
# print(kata.isalpha())

## Method isalnum() untuk mengecek apakah dalam sebuah string berisi huruf alfabet numerik, seperti hanya huruf atau hanya angka atau berisi keduanya ##
# kata = 'persona123'
# print(kata.isalnum())

## Method isdecimal() untuk mengecek dalam sebuah string hanya berisi angka ##
# print('123'.isdecimal())

## Method isspace() akan mengembalikan nilai True jika string hanya berisi whitespace ##
# print('         '.isspace())

## Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. ##
# print('Gundala Petir'.istitle())

