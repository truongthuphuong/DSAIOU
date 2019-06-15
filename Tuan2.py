#CAU9
print("Công thức tính:")
import math
C = 50
H = 30
print("Nhập vào giá trị D:")
Dlist = [100,150,180]
print("Dlist")
Q = math.sqrt ((2*C*Dlist)/H)
print ("Q =", round( Q, 0))
#CAU11
str = input("Nhap vao mot chuoi voi dau phan cach la ',':  ").split(',')
str.sort()
print (str)
#CAU12
str = input("Nhập vào chuỗi bất kì:")
print ("str.capitalize() : ", str.upper())
#CAU13
words = [word for word in input("Nhap vao chuoi cua ban: ").split(",")]
print (" ".join(sorted(list(set(words)))))
