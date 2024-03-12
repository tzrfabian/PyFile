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

# numbers = [1,2,3,4,5]
# for num in numbers:
#     if num == 5:
#         print("Angka ditemukan, Program berhenti!")
#         break
# else:
#     print('Angka tidak ditemukan.')
    
# print('\n')

# count = 0
# while count < 3:
#     print("Repeat")
#     count +=1
# else:
#     print('Blok else dieksekusi karena kondisi pada while salah (3<3 == False).')

# secret_word = "goyo"
# cntr = 0
# while True:
#     word = input("Input the Secret Word: ").lower()
#     cntr += 1
#     if word == "goyo":
#         print("Secret word was found, Mission Success!")
#         break
#     elif word != "goyo" and cntr > 6:
#         print("Mission failed, secret word can't found!")
#         break

# n = 10
# while n > 0:
#     n -= 1
#     if n == 5:
#         break
#     print(n)
# else:
#     print("Loop selesai!")

## list comprehension
# number = [1, 2, 3, 4]
# power = []

# for n in number:
#     power.append(n**2)
# print(power)
## alternative way
# number = [1, 2, 3, 4]
# power = [n**2 for n in number]
# print(power)

evenNumber = [n for n in range(501) if n % 2 == 0]
print(evenNumber)