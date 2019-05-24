# Chương trình xuất ra mảng 2 chiều
# Giá trị phần tử tại hàng i cột j phải là i * j

x = int(input("Nhap vao so hang: "))
y = int(input("Nhap vao so cot: "))
arr_2D = [[i * j for i in range(y)] for j in range(x)]

for i in range(x):
    for j in range(y):
        print(arr_2D[i][j], end="\t")
    print("\n")
