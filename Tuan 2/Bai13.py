# Chương trình nhập vào một chuỗi các từ cách nhau 1 space
# Xuất ra màn hình chuỗi vừa nhập loại bỏ các từ trùng nhau
s = input("Nhap vao mot chuoi: ")

list_old = s.split(" ")
list_new = sorted(set(list_old))

print(" ".join(list_new))
