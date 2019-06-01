'''Chuong trinh cho phep tim cac so le trong chuoi so duoc nhap vao'''

s=input("Moi nhap chuoi so cach nhau boi dau phay: ")
result=[x for x in s.split(',')if int(x)%2!=0]
print(result)