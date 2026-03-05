def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"

    for char in s:
        if char in vowels:
            count += 1

    return count


text = input("Nhap chuoi: ")
print("So nguyen am:", count_vowels(text))