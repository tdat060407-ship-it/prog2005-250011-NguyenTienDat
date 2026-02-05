n = int(input("Nhập số: "))
tong = 0

while n > 0:
    tong += n % 10
    n //= 10

print("Tổng các chữ số:", tong)
