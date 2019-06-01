'''Dau vao la day nhi phan 4 chu so
    Xuat ra cac day nhi phan chia het cho 5'''

result =[]
list1=[x for x in input("Moi nhap day nhi phan: ").split(',')]

for i in list1:
    temp=int(i,2)
    if temp % 5 == 0:
        result.append(i)

print(','.join(result))