#1
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)

bmi = round(bmi, 2)

print("BMI của bạn là : ", bmi)

#2
n = int(input("Nhập một số : "))

tổng = 0

while n > 0:
    digit = n % 10
    tổng += digit
    n //= 10

print("Tổng các chữ số là :", tổng)

#3
name = input("Nhập tên : ")

name = name.title()
name = name.lower()
name = name.strip()

print("Tên sau khi chuẩn hóa :", name)

#4
s = input("Nhập chuỗi : ")

upper = 0
lower = 0
special = 0
space = 0
vowel = 0
consonant = 0

vowels = "aeiouAEIOU"

for ch in s :
    if ch.isuper():
        upper += 1
    elif ch.islower():
        lower += 1

    if ch.isdigit():
        digit += 1

    if ch.isspace():
        space += 1

    if ch.isalpha():
        if ch in vowels:
            vowel += 1
    else:
            consonant += 1

    if not ch.isalnum() and not ch.isspace():
        special += 1

print("Chữ in hoa :", upper)
print("Chữ in thường :", lower)
print("Chữ số :", digit)
print("Ký tự đặc biệt :", special)
print("Khoảng trắng :", space)
print("Nguyên âm :", vowel)
print("Phụ âm :", consonant)

#5
class User:
    def __init__(self, id):
        self.id = id

    @property
    def id(self):
        return self._id

u = User(101)

print("ID của user:", u.id)

u.id = 200

#6
class product :
    def __init__(self, price):
        self.price = price

    @price.setter
    def price(self, value):
        if value > 0:
            self.price = value
        else:
            print("Giá trị phải lớn hơn 0")

    def _str_(self):
        return f"Price của product là : {self.price}"

p = Product(15.5)

print(p)

#7
class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_name(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p = person.from_string("Nam-20")

p.display()

#8
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def _str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2

print ("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v3)

#9
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Gâu Gâu")

d = Dog("Độ mixi")

print("Tên con chó:", d.name)
d.sound()

#10
class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    # Nạp chồng toán tử ==
    def __eq__(self, other):
        return self.diem == other.diem


# Tạo đối tượng
sv1 = SinhVien(8)
sv2 = SinhVien(8)
sv3 = SinhVien(7)

# So sánh
print(sv1 == sv2)  # True
print(sv1 == sv3)  # False

#11
class SinhVien:
    count = 0   # biến lớp

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1

    @classmethod
    def dem_so_sinh_vien(cls):
        return cls.count


# Tạo đối tượng
sv1 = SinhVien(8)
sv2 = SinhVien(7)
sv3 = SinhVien(9)

# In số sinh viên
print("Số đối tượng SinhVien được tạo:", SinhVien.dem_so_sinh_vien())









