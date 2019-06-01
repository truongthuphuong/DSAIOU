'''Nguoi dung nhap vao mot chuoi
    Chuong trinh cho phep xuat ra man hinh chuoi da nhap in hoa '''

list1=[]

while True:
    s=input("your list: ")
    if s:
        list1.append(s.upper())
    else:
        break

for i in range(len(list1)):
    print(list1[i])
