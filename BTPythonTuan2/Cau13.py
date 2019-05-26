s = input('Nhập chuỗi cách nhau bởi khoảng trắng: ').split(' ')
s = list(set(s))
s.sort()
print(' '.join(s))