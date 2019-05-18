x = int(input('Nhập x:'))
def giai_thua(x):
    if x == 0:
        return 1
    return x*giai_thua(x-1)
print(giai_thua(x))
