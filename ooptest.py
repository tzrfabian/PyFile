class Motor:
    def __init__(self, warna, merek, topspeed) -> None:
        self.warna = warna
        self.merek = merek
        self.topspeed = topspeed
        
    # @staticmethod
    # def intro_motor():
    #     print("This is method from class Motor")
        
    @classmethod
    def intro_motor(cls):
        print("This is method from class Motor")
    
    # @classmethod
    # def intro_motor(*args):
    #     print(args)
    
    def tambah_topspeed(self):
        self.topspeed += 10

Motor.intro_motor()        
print("Sebelum top speed ditambahkan")
motor_1 = Motor('Pink', 'Kawasaki', 140)
motor_2 = Motor('Red', 'Honda', 120)
motor_1.intro_motor()

print(motor_1.topspeed)
print(motor_2.topspeed,'\n')

motor_1.tambah_topspeed()
motor_2.tambah_topspeed()

print("Setelah top speed ditambahkan")
print(motor_1.topspeed)
print(motor_2.topspeed)

print('\n')

def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()