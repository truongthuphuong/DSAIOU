'''Chuong trinh cho phep xuat ra cac so tu 0 den n va chia het cho 7'''
def listNum(n):
    for i in range(n):
        if i % 7 == 0:
            yield i
x=int(input("Nhap so n ma ban muon xuat: "))

for i in listNum(x):
    print(i)

