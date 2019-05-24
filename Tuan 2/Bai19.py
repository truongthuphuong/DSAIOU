# Chương trình cho người dùng nhập vào 1 list
# In kết quả là 1 list các số lẻ từ những số người dùng nhập

n = int(input("Ban muon bao nhieu chu so trong mang: "))
list_number = []

print("Nhap vao {0} phan tu: ".format(n))
for i in range(n):
    x = int(input())
    list_number.append(x)


list_kq = [str(i) for i in list_number[:] if i % 2 != 0]
print("Cac so le trong mang la: {0}".format(",".join(list_kq)))
