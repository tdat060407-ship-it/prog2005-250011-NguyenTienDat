m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

A = []
B = []

print("Nhap ma tran A:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("Nhap ma tran B:")
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Ma tran tong:")
for row in C:
    print(row)