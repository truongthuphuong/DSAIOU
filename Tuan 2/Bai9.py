# Chuong trình nhập vào một chuỗi số
# Và trả về chuỗi kết quả theo công thức Q = √([(2*C*D)/H])
from math import *

C = 50
H = 30
D = input("Nhap vao mot day so cach boi dau phay: ")
list_numbers = D.split(",")
list_kq = []


def tinh_toan(list_numbers):
    """ Ham dung de tinh mot so theo cong thu
    cho san la Q = √([(2*C*D)/H])"""
    for i in list_numbers[:]:
        x = sqrt(((2 * C * int(i)) / H))
        list_kq.append(str(round(x)))


if __name__ == '__main__':
    tinh_toan(list_numbers)
    print(",".join(list_kq))
