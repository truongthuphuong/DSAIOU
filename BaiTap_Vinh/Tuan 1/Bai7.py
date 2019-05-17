# Chương trình in ra tài liệu của các hàm abs(), int(), intput()
# Thêm tài liệu cho hàm tự định nghĩa


def kiem_tra(str):
    """ Ham dung de kiem tra chuoi vua nhap
    co phai la mot chuoi doi xung hay khong """
    for i in range(int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
        return True


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
print(kiem_tra.__doc__)
