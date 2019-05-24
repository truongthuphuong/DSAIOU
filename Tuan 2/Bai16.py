# Chương trình nhập vào 1 chuỗi
# In ra chuỗi vừa nhập có bao nhiên số và chữ cái
s = input("Nhap vao 1 chuoi: ")
n_numbers = 0
n_letters = 0


for i in s[0:len(s)]:
    if i.isdigit():
        n_numbers = n_numbers + 1
    elif i.isalpha():
        n_letters = n_letters + 1
    else:
        pass


print("So chua cai la: {0}".format(n_letters))
print("So chu so la: {0}".format(n_numbers))
