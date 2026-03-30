#1
try:
    num = int(input("Nhập một số: "))
    print("Số dư khi chia cho 2 là:", num % 2)
except ValueError:
    print("Lỗi: Bạn phải nhập một số hợp lệ!")

#2
s = input("Nhập chuỗi: ")

print("Chuỗi đã nhập:", s)
print("Chuỗi in hoa:", s.upper())

#3
i = 1
tong = 0

while i <= 30:
    if i % 2 != 0:
        print(i, end=" ")
        tong += i
    i += 1

print("\nTổng các số lẻ:", tong)

#4
def tong_de_quy(n):
    if n == 1:
        return 1
    return n + tong_de_quy(n - 1)

n = int(input("Nhập n: "))
print("Tổng từ 1 đến n là:", tong_de_quy(n))

#5
class Flower:
    def __init__(self, color):
        self._color = color   # thuộc tính private

    # Getter
    def get_color(self):
        return self._color

    # Setter
    def set_color(self, color):
        self._color = color


# Tạo đối tượng
f = Flower("Red")

# Dùng getter
print("Màu ban đầu:", f.get_color())

# Dùng setter
f.set_color("Yellow")

print("Màu sau khi đổi:", f.get_color())