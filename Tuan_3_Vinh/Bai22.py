# Chương trình cho người dùng nhập vào name, age, score
# In ra màn hình theo thứ tự tăng dân ưu tiên là tên > tuổi > điểm
from operator import *

list_obj = []

print("Nhap vao ten,tuoi,diem: ")

while True:
    s = input()
    if (s == ""):
        break
    else:
        list_obj.append(tuple(s.split(",")))

print(sorted(list_obj, key=itemgetter(0, 1, 2)))
