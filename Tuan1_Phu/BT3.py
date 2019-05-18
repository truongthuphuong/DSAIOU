x = int(input('Nhap vao so can xuat dic:'))

tudien = {}


def tu_dien(x):
    for i in range(1, x + 1):
        tudien[i] = i * i
    return tudien


print("Dictionary cua so %d la: %s" % (x, tu_dien(x)))
