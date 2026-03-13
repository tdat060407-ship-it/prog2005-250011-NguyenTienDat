class Product:
    def __init__(self, price):
        self._price = price

    # getter
    def get_price(self):
        return self._price

    # setter
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Giá phải lớn hơn 0")

    # hàm in thông tin
    def __str__(self):
        return "Price: " + str(self._price)


# Tạo đối tượng
p1 = Product(100)

# In thông tin product
print(p1)

# Thử thay đổi giá
p1.set_price(200)
print(p1)