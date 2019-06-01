'''nguoi dung nhap vao mot mang 2 chieu
    va xuat ra mang 2 chieu voi gia tri hang thu i cot thu j la i*j'''
import numpy as np

x,y = int(input("so dong: ")),int(input("so cot: "))
a=np.zeros((x,y))

for i in range(x):
    for j in range(y):
        a[i][j]=i*j
print(a)