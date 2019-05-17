x=int(input('Nhap so di: '))
def giaithua(x):
    if(x==1):
        return 1
    else:
        return x*giaithua(x-1)
print("Giá trị của số:",giaithua(x))
