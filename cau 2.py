x = int(input('nhap so:'))
def giaithua(i):
    if(i == 0):
        return 1
    return x*giaithua(i-1)
print(giaithua(x))
