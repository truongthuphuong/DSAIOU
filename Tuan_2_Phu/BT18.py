'''Chuong trinh cho pheo tinh so gia tri a nhap vao: a+aa+aaa+aaaa = 1234'''

a=input("Moi nhap so a: ")

n1=int("%s"%a)
n2=int("%s%s"%(a,a))
n3=int("%s%s%s"%(a,a,a))
n4=int("%s%s%s%s"%(a,a,a,a))

print("Tong dang a+aa+aaa+aaaa: ",n1+n2+n3+n4)




