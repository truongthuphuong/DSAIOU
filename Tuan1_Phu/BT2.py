# tinh giai thua

x = int(input("nhap so can tinh:"))


def tinhgiaithua(x):
    if(x == 0):
        return 1
    else:
        return x * tinhgiaithua(x - 1)


print("giai thua cua so %d la: %d" % (x, tinhgiaithua(x)))
