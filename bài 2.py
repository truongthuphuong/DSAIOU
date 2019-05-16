x = int(input("nhập x:"))
def giaithua(x):
    if x == 0:
        return 1
    return x*giaithua(x-1)
print ("kết quả là:", giaithua(x))