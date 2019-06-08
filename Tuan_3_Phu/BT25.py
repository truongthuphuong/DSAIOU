'''Chuong trinh cho phep tinh tan xuat xuat hien cac tu trong input'''

re={}
s=input("moi ban nhap chuoi ").split()
for i in s:
    re[i]=re.get(i,0)+1

s1=sorted(re.keys())
for i in s1:
    print("%s:%d"%(i,re[i]))