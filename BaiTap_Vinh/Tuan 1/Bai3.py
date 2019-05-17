# Chương trình tạo ra Dictionary
number = int(input("Nhap vao so ban muon in ra Dictionary: "))
dict_1 = {}


def tao_thu_vien(n):
    for i in range(1, n + 1):
        dict_1[i] = i * i
    return dict_1


print(tao_thu_vien(number))
