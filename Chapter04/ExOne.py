def thong_ke(t):
    tong = 0
    lon_nhat = t[0]
    nho_nhat = t[0]

    for i in t:
        tong = tong + i

        if i > lon_nhat:
            lon_nhat = i

        if i < nho_nhat:
            nho_nhat = i

    return tong, lon_nhat, nho_nhat

# Ví dụ
t = (3, 7, 2, 9, 5)

kq = thong_ke(t)

print("Tổng:", kq[0])
print("Giá trị lớn nhất:", kq[1])
print("Giá trị nhỏ nhất:", kq[2])