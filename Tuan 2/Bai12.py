# Chương trình nhâp các dòng chữ
# In hoa và xuất ra các dong chuỗi vừa nhập
list_s = []
print("Nhap vao mot chuoi: ")

while True:
    s = input()
    if (s == ""):
        break
    else:
        list_s.append(s.upper())

print("\n".join(list_s))
