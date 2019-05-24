# Chương trình nhập vào 1 số
# In ra kết quả theo công thức a+aa+aaa+aaaa
n = int(input("Nhap vao 1 so nguyen: "))

n1 = str(n)
n2 = str(n + n)
n3 = str(n + n + n)
n4 = str(n + n + n + n)

print("Ket qua cua ban la: {}".format(n1 + n2 + n3 + n4))
