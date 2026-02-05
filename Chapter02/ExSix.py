def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

n = int(input("Nhập số: "))
print("Giai thừa =", giaithua(n))
