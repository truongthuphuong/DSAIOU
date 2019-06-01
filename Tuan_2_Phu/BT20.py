'''chuong trinh tinh so tien thuc dua tren nhat ki giao dich'''

TongTien=0

while True:
    s=input("Nhat ki giao dich (dang D (sotien) hoac W (sotien): ")
    if s=="":
        break
    s1=s.split(' ')
    Dang=s1[0]
    SoTien=int(s1[1])
    if Dang=="D":
        TongTien+=SoTien
    elif Dang=="W":
        TongTien-=SoTien
    else:
        pass
print("So tien sau khi giao dich la: ",TongTien)


