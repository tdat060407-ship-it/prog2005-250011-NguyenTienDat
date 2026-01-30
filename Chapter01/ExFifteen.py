name = input("Nhập tên sinh viên: ")
toan = float(input("Điểm Toán: "))
ly = float(input("Điểm Lý: "))
hoa = float(input("Điểm Hóa: "))

avg = (toan + ly + hoa) / 3

print("Tên:", name)
print("Điểm trung bình:", round(avg, 2))
