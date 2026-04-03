#1
PI = 3.14

r = float(input("Nhập bán kính: "))

chu_vi = 2 * PI * r

print("Chu vi hình tròn là:", chu_vi)

#2
names = []

for i in range(5):
    name = input(f"Nhập tên thứ {i+1}: ")
    names.append(name)

print("Danh sách ban đầu:", names)

del names[1]

print("Danh sách sau khi xóa phần tử thứ 2:", names)

#3
# Nhập mảng
arr = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))

# --- Số lẻ ---
so_le = []
for x in arr:
    if x % 2 != 0:
        so_le.append(x)

print("Các số lẻ:", so_le, "- Số lượng:", len(so_le))


# --- Kiểm tra số nguyên tố ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Lọc số nguyên tố
so_nguyen_to = []
for x in arr:
    if is_prime(x):
        so_nguyen_to.append(x)

print("Các số nguyên tố:", so_nguyen_to)

#4
class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, price):
        self.__price = price


book1 = Book("Book 1", 30000)

print("Giá sách:", book1.get_price())

#5
books = [
    ("Book 1", 30000),
    ("Book 2", 50000),
    ("Book 3", 100000)
]

tong = 0

with open("books.txt", "w", encoding="utf-8") as f:
    for name, price in books:
        f.write(f"{name};{price}\n")
        tong += price

    f.write(f"Tong;{tong}")

#6
layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}

print("layer-12:", layers["layer-12"])
print("layer-31:", layers["layer-11"]["layer-22"]["layer-31"])