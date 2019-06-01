# Yêu cầu nhập vào chuỗi các mật khẩu cách nhau bởi giấu phẩy
# Sau đó in ra màn hình mật khẩu nào đủ tiêu chuẩn
import re

s = input("Nhap vao cac mat khau cach nhau boi giau phay: ")
list_mk = s.split(",")
list_kq = []


for i in list_mk[:]:
    if len(i) >= 6 or len(i) <= 12:
        if not re.search("[a-z]", i):
            continue
        elif not re.search("[A-Z]", i):
            continue
        elif not re.search("[0-9]", i):
            continue
        elif not re.search("[$@#]", i):
            continue
        else:
            pass
    else:
        pass
    list_kq.append(i)


print(",".join(list_kq))
