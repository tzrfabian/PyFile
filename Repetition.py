# for i in range (10):
#     print(i)

# for i in range (1,11,2):
#     print(i)

# print('\n')
    
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1 
    
# for i in range (1,3):
#     for j in range (1,3):
#         print(i,j)

# for i in range(2):  # Perulangan tingkat pertama
#     print("Perulangan luar:", i)
#     for j in range(10):  # Perulangan tingkat kedua
#         print("Perulangan dalam:", j)
#         if j == 1:
#             break  # Menghentikan perulangan dalam jika j = 1

# print ('\n')

# for huruf in 'Dico ding':
#     if huruf == ' ':
#         continue
#     print('Huruf saat ini: {}'.format(huruf))

numbers = [1,2,3,4,5]
for num in numbers:
    if num == 5:
        print("Angka ditemukan, Program berhenti!")
        break
else:
    print('Angka tidak ditemukan.')
    
print('\n')

count = 0
while count < 3:
    print("Repeat")
    count +=1
else:
    print('Blok else dieksekusi karena kondisi pada while salah (3<3 == False).')