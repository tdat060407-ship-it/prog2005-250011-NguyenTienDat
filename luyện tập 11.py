#1
arr = []
for i in range (5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    arr.append(s)

print("\nMảng ban đầu: ", arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    print(f"\nBước {i}: ")
    print("key =", key)

    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1
        print(" Dịch chuyển:", arr)

    arr[j + 1] = key
    print(" Chèn key:", arr)

print("\nKết quả cuối cùng:", arr)

#2
# Nhập chuỗi cần tìm
x = input("Nhập chuỗi cần tìm: ")

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == x:
        print("Tìm thấy tại vị trí:", mid)
        break
    elif len(arr[mid]) < len(x):
        right = mid - 1   # vì giảm dần
    else:
        left = mid + 1
else:
    print("Không tìm thấy")

#3
nums = list(map(int, input("Nhập các số: ").split()))

tong = 0

print("Các số chẵn là: ")
for x in nums:
    if x % 2 == 0:
        print(x, end=" ")
        tong += x

print("\nTổng các số chẵn là:", tong)

#4
arr = []

n = int(input("Nhập số lượng phần tử: "))

for i in range (n):
    x = int(input("Nhập số: "))
    arr.append(x)

print("Danh sách:", arr)

k = int(input("Nhập k: "))
dem = arr.count(k)
print("Số lần xuất hiện của", k, "là:", dem)

def la_snt(x):
    if x < 2:
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

tong = 0
for x in arr:
    if la_snt(x):
        tong += x

print("Tổng các số nguyên tố:", tong)

arr.sort()
print("Danh sách sau khi sắp xếp:", arr)

arr.clear()
print("Danh sách sau khi xóa:", arr)

#5
d ={
    "a": 1,
    "b": 2,
    "c": 3
}

key = input("Nhập key: ")

if key in d:
    print("Key tồn tại trong dictionary: ")
else:
    print("Key không tồn tại ")

#6
d = {}

n = int(input("Nhập số người:"))

for i in range(n):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    d[ten] = tuoi

print("Danh sách: ", d)

tong = sum(d.values())
tb = tong / n

print("Tuổi trung bình:", tb)

#7
import csv

ten = input("Nhập tên nhân viên: ")
tuoi = input("Nhập tuổi: ")
id_nv = input("Nhập ID: ")

with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write("Tên: " + ten + "\n")
    f.write("Tuổi: " + tuoi + "\n")
    f.write("ID: " + id_nv + "\n")

print("Đã lưu file nhanvien.txt")

with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Ten", "Tuoi", "ID"])
    writer.writerow([ten, tuoi, id_nv])

print("Đã lưu file nhanvien.csv")

#8
sv = ("Duc", 100, 5)

ten, tuoi, diem = sv

print("Tên:", ten)
print("Tuổi:", tuoi)
print("Điểm trung bình:", diem)

#9
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = []
print("Nhập ma trận A:")
for i in range(m):
    row = []
    for j in range(n):
        x = input(f"A[{i}][{j}] = ")
        if x == "":
            print("Lỗi: không được để trống!")
            exit()
        row.append(int(x))
    A.append(row)

B = []
print("Nhập ma trận B:")
for i in range(m):
    row = []
    for j in range(n):
        x = input(f"B[{i}][{j}] = ")
        if x == "":
            print("Lỗi: không được để trống!")
            exit()
        row.append(int(x))
    B.append(row)

C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# In kết quả
print("Ma trận tổng:")
for row in C:
    print(row)

