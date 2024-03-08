belanjaan1 = "Daging ayam"
ketersediaan = True #False
if ketersediaan == True:
    print(f"Ibu membeli dan memasak {belanjaan1}")
else:
    print(f"Ibu membeli dan memasak Telur Goreng")
    

height = 146
if height >= 150:
    print("You are allowed to ride a rollercoaster")
else:
    print("You are not allowed to ride rollercoaster")
    
print("\n")

nilai = 80
if nilai >= 85:
    print("Grade A")
    print("Pertahankan!")
elif nilai >= 80:
    print("Grade B")
    print("Tingkatkan!")
elif nilai >= 70:
    print("Grade C")
    print("Perbaiki!")
elif nilai >= 60:
    print("Grade D")
    print("Remedial!")
    
lulus = 90
print("Selamat lulus!")if lulus == 100 else print("Ngulang!")
print('\n')

score = 82
attitude = "baik"

if nilai >= 80 and attitude == "baik":
    print("Nilai kamu bagus dan perilaku kamu baik!")
elif nilai >= 80 and attitude != "baik":
    print("Nilai kamu bagus, tetapi perilaku mu buruk")