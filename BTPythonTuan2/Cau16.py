s = input("Nhập chuỗi: ")
def kiem_tra_chuoi(s):
    dem_num = 0
    dem_alpha = 0
    for i in range(len(s)):
        if s[i].isalpha():
            dem_alpha += 1
        else:
            if s[i].isdigit():
                dem_num += 1
    print("Chữ thường:", dem_alpha,"\nChữ số:", dem_num)


kiem_tra_chuoi(s)