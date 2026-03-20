#1
def lay_ten_file(path):

    danh_sach = path.split("\\")

    ten_file = danh_sach[len(danh_sach)-1]

    return ten_file

def lay_ten_bai_hat(path):
    danh_sach = path.split("\\")
    ten_file = danh_sach[len(danh_sach)-1]

    danh_sach2 = ten_file.split(".")
    ten_bai = danh_sach2[0]

    return ten_bai

s = "d:\\music\\muabui.mp3"
print(lay_ten_file(s))
print(lay_ten_bai_hat(s))

#2
chuoi = input("Nhập chuỗi:")
ky_tu = input("Nhập ký tự cần đếm :")

dem = 0

for c in chuoi :
    if c == ky_tu :
        dem = dem + 1

print("Số lần xuất hiện là : ", dem)

#3
def giai_thua(n):
    if n == 0 or n ==1 :
        return 1
    return n * giai_thua(n - 1)

n = int(input("Nhập số n : "))

if n < 0 :
    print("Không có giai thừa số âm ")
else:
    print("Giai thua la :", giai_thua(n))

#4
chuoi = input("Nhập chuỗi: ")

if chuoi == "":
    print("Lỗi: Bạn chưa nhập chuỗi!")
else:
    do_dai = len(chuoi)
    print("Độ dài của chuỗi là:", do_dai)

#5
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)

plt.figure()

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Do thi y = x^2 ")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Do thi y = sqrt(x) ")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

#6
chuoi = input("Nhập chuỗi: ")

dao = ""

for i in range(len(chuoi) -1, -1, -1):
    dao = dao + chuoi[i]

print("Chuỗi đảo là:", dao)

#7
mat_khau_dung = ("Duc ngu 2k7")
mat_khau = input("Nhập mật khẩu: ")

while mat_khau != mat_khau_dung:
    print("Sai mật khẩu, thử lại! ")
    mat_khau = input("Nhập lại mật khẩu: ")

print("Đăng nhập thành công ")

#8
ds = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1} : ")
    ds.append(s)

print("\nDanh sách ban đầu: ", ds)

n = len(ds)
for i in range (n):
    print(f"\n--- Bước {i+1} ---")
    for j in range(0, n - i - 1):

        if len(ds[j]) < len(ds[j + 1]):

            ds[j], ds[j + 1] = ds[j + 1], ds[j]

        print(ds)

print("\nDanh sách sau khi sắp xếp:", ds)

#9
class Person:

    count = 0

    def __init__(self, name, age):
        if age < 0:
           raise ValueError ("Tuổi phải lớn >= 0")

        self.name = name
        self.age = age
        Person.count += 1

    def get_name (self):
        return self._name

    def get_age (self):
        return self._age

    def set_age(self, age):

        if age < 0:
            raise ValueError("Tuổi không hợp lệ ")
        self._age = age

    def __str__ (self):
        return (f"Name: {self.name}, Age: {self._age}")

    def say_hello(self):
        return f"Xin chào, tôi là {self._name}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self._age == other._age


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)

        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0 đến 10")

        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, score):
        if score < 0 or score > 10:
            raise ValueError("Điểm không hợp lệ")
        self._score = score

    def __str__(self):
        return f"{super().__str__()}, Score: {self._score}"

    def study(self):
        return f"{self._name} đang học bài"

try:
    p1 = Person("An", 20)
    p2 = Person("Bình", 20)

    s1 = Student("Cường", 18, 8)

    print(p1)
    print(s1)

    print("Tên:", p1.get_name())

    p1.set_age(25)
    print("Tuổi mới:", p1.get_age())

    print(p1.say_hello())
    print(s1.study())

    print("Số đối tượng:", Person.get_count())

    print("p1 == p2:", p1 == p2)

except ValueError as e:
    print("Lỗi:", e)

#10
def dem_ky_tu():
    chuoi = input("Nhập chuỗi: ")
    ky_tu = input("Nhập ký tự: ")

    dem = 0
    for c in chuoi:
        if c == ky_tu:
            dem += 1

    print("Số lần xuất hiện:", dem)


def giai_thua():
    def de_quy(n):
        if n == 0 or n == 1:
            return 1
        return n * de_quy(n - 1)

    n = int(input("Nhập n: "))
    if n < 0:
        print("Không hợp lệ")
    else:
        print("Giai thừa:", de_quy(n))


def dao_chuoi():
    chuoi = input("Nhập chuỗi: ")
    dao = ""

    for i in range(len(chuoi) - 1, -1, -1):
        dao += chuoi[i]

    print("Chuỗi đảo:", dao)


def nhap_mat_khau():
    mk_dung = "python123"

    while True:
        mk = input("Nhập mật khẩu: ")
        if mk == mk_dung:
            print("Đúng mật khẩu!")
            break
        else:
            print("Sai, nhập lại!")

while True:
    print("\n===== MENU =====")
    print("1. Đếm ký tự trong chuỗi")
    print("2. Tính giai thừa (đệ quy)")
    print("3. Đảo ngược chuỗi")
    print("4. Nhập mật khẩu")
    print("0. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        dem_ky_tu()
    elif choice == "2":
        giai_thua()
    elif choice == "3":
        dao_chuoi()
    elif choice == "4":
        nhap_mat_khau()
    elif choice == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")








