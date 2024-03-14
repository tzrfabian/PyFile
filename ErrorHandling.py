# n=2
# try:
#     z = int(input("Insert number: "))
#     print(n/z)
# except ZeroDivisionError:
#     print("Cannot divide any number with Zero number.")
    
# var_dict = {"rata_rata": "2.5"}

# try:
#     print(f"rata-rata adalah {var_dict['rata_rata']}")
# except KeyError:
#     print("Key tidak ditemukan.")
# except TypeError:
#     print("Anda tidak bisa membagi nilai dengan tipe data string")
# else:
#     print("Kode ini dieksekusi jika tidak ada exception.")
# finally:
#     print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

## Raise exception
var = 10
# var = -10
if var < 0:
    raise ValueError("Negative number not allowed!")
else:
    for i in range (var):
        print(i+1)