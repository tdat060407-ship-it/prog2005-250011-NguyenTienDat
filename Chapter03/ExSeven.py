arr = list(map(int, input("Nhap danh sach so: ").split()))
x = int(input("Nhap so can tim: "))

index = -1

for i in range(len(arr)):
    if arr[i] == x:
        index = i
        break

if index != -1:
    print("Vi tri cua so:", index)
else:
    print("Khong tim thay")