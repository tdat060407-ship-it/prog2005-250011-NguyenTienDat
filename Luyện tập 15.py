#1
# Nhập hai số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b

# Kiểm tra chia cho 0
if b != 0:
    thuong = a / b
else:
    thuong = "Không chia được (b = 0)"

# In kết quả
print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)

#2
def hello(name="Student"):
    print("Xin chào,", name)

# Gọi hàm
hello()            # Không truyền đối số
hello("Đạt")       # Có truyền đối số

#3
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

n = int(input("Nhập số: "))
print("Giai thừa:", giai_thua(n))

#4
d1 = float(input("Nhập điểm môn 1: "))
d2 = float(input("Nhập điểm môn 2: "))
d3 = float(input("Nhập điểm môn 3: "))

tb = (d1 + d2 + d3) / 3

print("Điểm trung bình:", tb)

if tb >= 8:
    print("Xếp loại: Giỏi")
elif tb >= 6.5:
    print("Xếp loại: Khá")
elif tb >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

#5
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

chuoi = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(chuoi))

#6
colors = ["đỏ", "xanh", "vàng", "tím", "đen"]

print("Danh sách ban đầu:", colors)

# Xóa một màu (ví dụ xóa 'vàng')
colors.remove("vàng")

print("Sau khi xóa:", colors)

#7
students = {
    "An": 8,
    "Bình": 7,
    "Cường": 9
}

def diem_trung_binh(d):
    return sum(d.values()) / len(d)

print("Điểm trung bình:", diem_trung_binh(students))

#8
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            print("Lỗi: Giá không hợp lệ!")
        else:
            self._price = price

# Test
p = Product(100)
print("Giá:", p.get_price())

p.set_price(-50)  # báo lỗi

#9
char = input("Nhập 1 ký tự: ")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(char)

print("Đã ghi vào file!")

#10
a = input("Nhập a: ")
b = input("Nhập b: ")

chuoi = f"{a}---{b}"

print(chuoi)