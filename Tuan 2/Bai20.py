# Chương trình tính số tiền thực của ngân hàng
# Dựa trên nhật kí giao dịch

tong_tien = 0
tien_gui = 0
tien_rut = 0

print("Nhap vao tien gui va tien rut: ")

while True:
    s = input()
    if (s == ""):
        break
    else:
        list_string = s.split(" ")
        if list_string[0] == "D":
            tien_gui = tien_gui + int(list_string[1])
        elif list_string[0] == "W":
            tien_rut = tien_rut + int(list_string[1])
        else:
            pass

tong_tien = tien_gui - tien_rut
print("Tong tien cua ban la: {0}".format(tong_tien))
