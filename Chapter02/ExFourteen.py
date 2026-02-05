n = int(input("Nhập số: "))

dem = 0
for i in range(1, n + 1):
    if n % i == 0:
        dem += 1

if dem == 2:
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")
