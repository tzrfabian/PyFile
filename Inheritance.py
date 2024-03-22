# class Mobil:
#     def __init__(self, color, brand, speed) -> None:
#         self.color = color
#         self.brand = brand
#         self.speed = speed
    
#     def up_speed(self):
#         self.speed += 15
        

# class MobilSport(Mobil):
#     def turbo(self):
#         self.speed += 45
    
#     def up_turbospeed(self):
#         super().up_speed()
#         self.speed += 10
#         print("Warning! You almost reach the speed limit. Becareful!")

# # Class Mobil Standard        
# mobil_1 = Mobil("Merah", "Mazda", 140)
# print(mobil_1.speed)
# mobil_1.up_speed()
# print(mobil_1.speed,'\n')

# # Class Mobil Sport       
# mobilsport_1 = MobilSport("Putih", "Honda", 160)
# print(mobilsport_1.speed)
# mobilsport_1.turbo()
# mobilsport_1.up_turbospeed()
# print(mobilsport_1.speed)

class Animal:
    def __init__(self, name, age, species) -> None:
        self.name = name
        self.age = age
        self.species = species
        
class Cat(Animal):
    def deskripsi(self):
        return f'{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun'
    
    def suara(self):
        return "meow!"
    
myCat = Cat("Neko", 3, "Persian")

print(myCat.deskripsi())
print(myCat.suara())
