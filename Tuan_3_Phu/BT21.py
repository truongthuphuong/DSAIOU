'''Chuong trinh cho phep kiem tra tinh hop le cua mat khau duoc nguoi dung nhap vao'''

import re
result = []
strings = [x for x in input("Moi nhap password: ").split(',')]

for i in strings:
    if len(i) < 6 or len(i) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]",i):
        continue
    elif not re.search("[0-9]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search("[$#@]",i):
        continue
    elif re.search(" ",i):
        continue
    else:
        pass
    result.append(i)

print(result)
