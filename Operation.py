## Method len() untuk menghitung panjang dari elemen, list & string ##
# list1 = [1,2,3,3,4,5,6,6,7,8,8,8,9]
# list2 = set([1,2,2,2,3,4,5,5,5]) ## list dikonversi menjadi set, sehingga nilai duplikat tidak dihitung
# string1 = "AbacusP"

# print(list1)
# print(len(list1))
# print(len(list2))
# print(string1)
# print(len(string1))

## Method min() & max() ##
# number = [13, 3, 24, 5, 96, 84, 71, 11, 38]

# print(min(number))
# print(max(number))

## Method count() untuk mengetahui berapa kali jumlah objek pada list/string
# even = [2, 4, 4, 6, 6, 6, 8, 10, 10]
# print(even.count(10))

# string = "Hari ini aku hanya makan roti lapis daging saja"
# substring = "a"
# print(string.count(substring))

## Operator in & not in diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list ##
# kalimat = "Belajar Python di Dicoding sangat menyenangkan"
# print('Dicoding' in kalimat)
# print('tidak' in kalimat)
# print('Dicoding' not in kalimat)
# print('tidak' not in kalimat)

## Contoh memberikan value untuk multiple variable ##
# data = ['shirt', 'white', 'L']
# apparel, color, size = data

# print(data)
# print(apparel)
# print(color)
# print(size)

## Function sort() untuk mengurutkan angka atau urutan huruf ##
# game = ['Persona', 'Mario', 'Assasins Creed', 'Battlefield', 'Far Cry']
# game.sort()
# print(game)

# game.sort(reverse=True) ## reverse = True untuk mengurutkan dari akhir/belakang
# print(game)

var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

panjang = len(var_list)
maksimal = max(var_list)
minimal = min(var_list)
banyak = var_list.count(605132)
print(banyak)