#1
a = 10
b = 4

result = (a**2 + b**2) / (a - b)
print(result)

#2
import math

#Nhập hai số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b :"))

#Lũy thừa
power = a**b

#Căn bậc 2
sqrt_a = math.sqrt(a)

#Chia lấy phần nguyên
div_int = a // b

#Chia lấy phần dư
mod = a % b

#Làm tròn số
round_a = round(a)

#In kết quả
print("Lũy thừa a^b =", power)
print("Căn bậc 2 của a =", sqrt_a)
print("Chia lấy phần nguyên a // b =", div_int)
print("Chia lấy phần dư a % b =", mod)
print("Làm tròn của a =", round_a)

#3
n = int(input("Nhập một số từ 1 đến 9"))

if 1 <= n <= 9:
    for i in range(1, 10):
        print(n, "x", i, "=", n * i)
else:
    print("Vui lòng nhập từ 1 đến 9")

#4
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)

#5
import random
m = int(input("Nhập số hàng M: "))
n = int(input("Nhập số cột N: "))

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)

r = int(input("Nhập số hàng muốn hiển thị: "))
if 1 <= r <= m:
    print("Hàng", r, ":", matrix[r-1])
else:
    print("Hàng không hợp lệ")

c = int(input("Nhập số cột muốn hiển thị: "))
if 1 <= c <= n:
    print("Cột", c, ":")
    for i in range(m):
        print(matrix[i][c-1])
else:
    print("Cột không hợp lệ")

max_value = matrix[0][0]
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

print("Giá trị lớn nhất trong ma trận:", max_value)

#6
# Nhập chuỗi
s = input("Nhập chuỗi số (vd: 5; 7; 8; -2; 8; 11; 13; 9; 10): ")

# Tách chuỗi thành danh sách số
numbers = [int(x.strip()) for x in s.split(";")]

# In từng số trên một dòng
print("Các số:")
for num in numbers:
    print(num)

# Đếm số chẵn
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

# Đếm số âm
negative_count = 0
for num in numbers:
    if num < 0:
        negative_count += 1

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Đếm số nguyên tố
prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

# Tính trung bình
avg = sum(numbers) / len(numbers)

# In kết quả
print("Số chẵn:", even_count)
print("Số âm:", negative_count)
print("Số nguyên tố:", prime_count)
print("Trung bình:", avg)

#7
# Tạo lớp Student
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Khởi tạo 2 đối tượng sinh viên
sv1 = Student("Độ mixue", 4)
sv2 = Student("Tú sena", 10)

# In thông tin
print("Sinh viên 1:", sv1.name, "-", sv1.score)
print("Sinh viên 2:", sv2.name, "-", sv2.score)

#8
class Student:
    def __init__(self, name, score):
        self.name = name

        if 0 <= score <= 10:
            self.score = score
        else:
            print("Điểm không hợp lệ (phải từ 0 đến 10)")
            self.score = 0


# Tạo 2 sinh viên
sv1 = Student("Trần Bình", 8.5)
sv2 = Student("Vũ Mạnh Cường", 12)

# In thông tin
print(sv1.name, sv1.score)
print(sv2.name, sv2.score)

#9
class Student:
    def __init__(self, name, score):
        self.name = name

        if 0 <= score <= 10:
            self.score = score
        else:
            print("Điểm không hợp lệ")
            self.score = 0

    # Phương thức hiển thị thông tin
    def display(self):
        print("Sinh viên", self.name, "có điểm là", self.score)


# Tạo 2 sinh viên
sv1 = Student("Tài enzo", 10)
sv2 = Student("Lai Bâng", 8)

# Gọi phương thức display
sv1.display()
sv2.display()

#10
# Tên tệp lưu dữ liệu
filename = "products.txt"

# Nhập sản phẩm và lưu vào tệp
code = input("Nhập mã sản phẩm: ")
name = input("Nhập tên sản phẩm: ")
price = float(input("Nhập giá sản phẩm: "))

with open(filename, "a", encoding="utf-8") as f:
    f.write(f"{code};{name};{price}\n")

print("Đã thêm sản phẩm vào tệp.\n")

# Đọc danh sách sản phẩm từ tệp
products = []
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        code, name, price = line.strip().split(";")
        products.append((code, name, float(price)))

# Hiển thị danh sách sản phẩm
print("Danh sách sản phẩm:")
for p in products:
    print(p[0], "-", p[1], "-", p[2])

# Sắp xếp theo giá giảm dần
products.sort(key=lambda x: x[2], reverse=True)

print("\nSản phẩm sau khi sắp xếp theo giá giảm dần:")
for p in products:
    print(p[0], "-", p[1], "-", p[2])








