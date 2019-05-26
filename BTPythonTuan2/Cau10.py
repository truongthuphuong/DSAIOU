s = input('Nhập X, Y: ').split(',')
row = int(s[0])
col = int(s[1])
arr = [[0 for j in range(col)] for i in range(row)]
print(arr)
for i in range(row):
    for j in range(col):
        arr[i][j] = i*j
print(arr)

