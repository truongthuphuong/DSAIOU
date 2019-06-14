import sys
tienGui = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    values = s.split(" ")
    tien = values[0]
    amount = int(values[1])
    if tien=="D":
         tienGui+=amount
    elif tien=="W":
        tienGui-=amount
    else:
        pass
print (tienGui)