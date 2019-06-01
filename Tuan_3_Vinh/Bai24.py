# Chương trình tính số đường đi của Robot
from math import *

print("""Nhap vao theo vi du:
    RIGHT 3
    LEFT 2
    UP 3
    DOWN 2 """)
print("Nhap vao di di chuyen cua robot: ")
vitri = [0, 0]  # toa do x, y

while True:
    s = input()
    if s == "":
        break
    else:
        m = s.split(" ")
        huong = m[0]
        buoc = int(m[1])
        if huong == "RIGHT":
            vitri[1] += buoc
        elif huong == "LEFT":
            vitri[1] -= buoc
        elif huong == "UP":
            vitri[0] += buoc
        elif huong == "DOWN":
            vitri[0] -= buoc
        else:
            pass

print("Robot vua di chuyen khoang cach la: {0}".format(
    int(round(sqrt(vitri[0] ** 2 + vitri[1] ** 2)))))
