# Chương trình nhập vào một chuỗi
# In ra màn hình số kí tự in hoa và thường
s = input("Nhap vao 1 chuoi: ")
n_upper = 0
n_lower = 0


for i in s[:]:
    if i.isupper():
        n_upper = n_upper + 1
    elif i.islower():
        n_lower = n_lower + 1
    else:
        pass

print("So ki tu hoa la: {0}".format(n_upper))
print("So ki tu thuong la: {0}".format(n_lower))
