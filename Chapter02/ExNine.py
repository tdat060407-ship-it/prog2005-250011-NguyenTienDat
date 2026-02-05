n = input("Nhập số 5 chữ số: ")

max_digit = int(n[0])
for ch in n:
    if int(ch) > max_digit:
        max_digit = int(ch)

print("Chữ số lớn nhất:", max_digit)
