colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except ValueError:
    print("Green khong co trong danh sach")

print("Danh sach sau khi xoa:", colors)