'''chuong trinh cho phep dem so chu cai va so chu so'''

s=input("Nhap chuoi cua ban: ")

c_digits=0
c_alpha=0

for i in s:
    if i.isdigit():
        c_digits+=1
    elif i.isalpha():
        c_alpha+=1
    else:
        pass

print("so chu cai la: ", c_alpha)
print("so chu so la: ", c_digits)