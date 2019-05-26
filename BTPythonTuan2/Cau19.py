s = input('Nhập các số cách nhau bởi dấu phẩy: ')
s = s.split(',')
print(s)
d = []
for i in range(len(s)):
    if int(s[i])%2==1:
        d.append(str(s[i]))

print(','.join(d))