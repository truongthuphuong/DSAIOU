'''Chuong trinh cho phep dem so chu hoa va so chu thuong'''

s=input("Moi nhap chuoi: ")

d={"Chu Hoa":0,"Chu Thuong":0}

for i in s:
    if i.isupper():
        d["Chu Hoa"]+=1
    elif i.islower():
        d["Chu Thuong"]+=1
    else:
        pass

print("so chu hoa la:", d["Chu Hoa"])
print("So chu thuong la: ",d["Chu Thuong"])
