'''chuong trinh cho phep nguoi dung nhap vao mot chuoi so gan vao gia tri D
    va xuat ra tung gia tri'''


from math import sqrt
C = 50
H = 30
D = (input("Chuoi cua ban la: "))
list1 = D.split(",")
list2 = []
for i in list1[:]:
    Q = (2 * C * int(i)) // H
    Q = sqrt(Q)
    list2.append(round(Q))

print(list2)
