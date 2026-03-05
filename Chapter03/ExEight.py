arr = list(map(int, input("Nhap danh sach so: ").split()))

found = False

for num in arr:
    if num > 10:
        print("So dau tien lon hon 10:", num)
        found = True
        break

if not found:
    print("Khong co so nao lon hon 10")