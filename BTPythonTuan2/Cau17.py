s = input("Nhập chuỗi: ")
def kiem_tra_chuoi(s):
    dem_title = 0
    dem_alpha = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].istitle():
                dem_title += 1
            else:
                dem_alpha += 1
    print("Chữ hoa:", dem_title,"\nChữ thường:", dem_alpha)


kiem_tra_chuoi(s)