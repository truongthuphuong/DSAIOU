# Chương trình sử dụng generator
# Cho người dùng nhập vào N xuất ra các số từ O đến N chia hết cho 7
n = int(input("Nhap vao n: "))


def numbers(n):
    i = 0
    while i < n:
        if i % 7 == 0:
            yield i
        i = i + 1


def in_man_hinh(n):
    for i in numbers(n):
        print(i)


in_man_hinh(n)
