# Tạo dictionary
sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

# Nhập tên cần kiểm tra
ten = input("Nhập tên sinh viên cần kiểm tra: ")

# Kiểm tra key có tồn tại hay không
if ten in sinh_vien:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại trong dictionary")