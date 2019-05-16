x = int(input("Nhập số:"))
def giaithua(x):
    if (x == 0):
        return 1
    return x * giaithua(x - 1)
print(giaithua(x))