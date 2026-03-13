# Tạo lớp Hoa
class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau


# Tạo đối tượng
hoa1 = Hoa("Hoa Hồng", "Đỏ")

# In thông tin hoa
print("Tên hoa:", hoa1.ten)
print("Màu hoa:", hoa1.mau)