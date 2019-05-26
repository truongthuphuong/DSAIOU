s = input('Nhập các chuỗi nhị phân: ')
s = s.split(',')
print(s)
d = []
for i in range(len(s)):
    if not(s[i].startswith('0')):
        s[i] = int(s[i])
        if s[i] % 5 == 0:
            d.append(s[i])

print(','.join(str(i) for i in d))
