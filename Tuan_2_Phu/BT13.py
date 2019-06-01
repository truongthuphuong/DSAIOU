'''Dau vao la mot chuoi tach biet boi khoang trang
    Chuong trinh xuat ra chuoi voi loai bỏ cac tu trung lap va sap xep theo bang chu cai'''

list1=[x for x in input("nhap vao chuoi: ").split(" ")]
list1=set(list1)
print(' '.join(sorted(list1)))