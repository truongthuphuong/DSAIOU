# Giai thừa

x = int(input("Mời nhập x: "))


def giaithua(x):
    if (x == 1) or (x == 0):
        return 1
    else:
        return x*giaithua(x-1)


print("Giai thừa của", x, "là: ", giaithua(x))




