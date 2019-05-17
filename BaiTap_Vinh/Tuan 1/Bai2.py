# Chương trình tính giai thừa của số do người dùng nhập vào
number = int(input("Nhap vao so muon tinh giai thua: "))


def giai_thua(n):
    if(n == 0):
        return 1
    else:
        return n * giai_thua(n - 1)


print(giai_thua(number))
