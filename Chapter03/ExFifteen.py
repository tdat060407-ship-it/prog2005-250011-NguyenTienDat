#1
s = input("Nhap chuoi: ")
print("Chuoi dao nguoc:", s[::-1])

#2
s = input("Nhap chuoi: ")

reverse = ""

for i in range(len(s)-1, -1, -1):
    reverse += s[i]

print("Chuoi dao nguoc:", reverse)