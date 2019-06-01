'''In cac phan tu trong chuoi nguoi dung nhap vao (phan cach nhau boi dau phay)
    Va in ra theo thu tu trong bang chu cai'''

list1=[x for x in input("Nhap vao chuoi tach boi dau phay:").split(',')]
print(','.join(sorted(list1)))