s = input("Nhập chuỗi: ")
c = input("Nhập ký tự cần đếm: ")

count = 0
for ch in s:
    if ch == c:
        count += 1

print("Số lần xuất hiện:", count)
