# Chương trình nhập vào chuỗi nhị phân 4 chữ số, cách dấu phẩy
# Xuất ra màn hình số nào chia hết cho 5 cách dấy phẩy

str_numbers = input("Nhap vao chuoi cac so nhi phan 4 chu so: ")
list_numbers = (str_numbers.split(","))
list_kq = []


def kiem_tra(list_numbers):
    for i in list_numbers[:]:
        decimal = int(i, 2)
        if decimal % 5 == 0:
            list_kq.append(i)


kiem_tra(list_numbers)
if len(list_kq) == 0:
    print("Khong co so nao chia het cho 5!")
else:
    print(",".join(list_kq))
