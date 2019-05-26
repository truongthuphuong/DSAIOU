from math import sqrt

Const_C=50
Const_H=30

D=input('nhap: ').split(',')
Q=list()
for i in D:
    Q.append(str(int(sqrt((2*Const_C*int(i))/Const_H))))

print(','.join(Q))