arr = list(map(int, input("Nhap danh sach so: ").split()))

swap_count = 0
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap_count += 1

print("Danh sach sau sap xep:", arr)
print("So lan hoan doi:", swap_count)