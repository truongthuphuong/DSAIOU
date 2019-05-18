# ham in mot so ham co ban
list_fib = []


def fib(n=int()):

    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def print_fib(n=int()):
    for i in range(n):
        list_fib.append(fib(i))
    print list_fib,


n = int(input("day so fib thu:"))
tong = 0
print_fib(n)
for i in range(n):
    tong = tong + fib(i)
print "va tong day so fib la: %d" % (tong)
print(print_fib().__doc__)
