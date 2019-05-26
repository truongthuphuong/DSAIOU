from math import sqrt
d = input('Nhập chuỗi giá trị của d: ')
d = d.split(',')
s = []


def CongThuc(d, c = 50, h = 30):
    for i in range(len(d)):
        d[i] = int(d[i])
        s.append(str(round(sqrt((2*c*d[i])/h))))
    print(','.join(s))


CongThuc(d)
