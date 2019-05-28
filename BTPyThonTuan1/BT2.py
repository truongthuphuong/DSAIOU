x=int(input("nhập vào 1 số cần tính: "))
def gt(x):
    if x == 0:
        return 1
    return x*gt(x-1)
print("giai thừa của ", x, " là: ", gt(x))

