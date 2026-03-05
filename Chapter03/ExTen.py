arr = list(map(int, input("Nhap danh sach so: ").split()))

sum_even = 0

print("Cac so chan:")
for num in arr:
    if num % 2 == 0:
        print(num)
        sum_even += num

print("Tong cac so chan:", sum_even)