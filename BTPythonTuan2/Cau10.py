c = input("Nhập X, Y: ")
dms=[int(x) for x in c.split(',')]
rowNum=dms[0]
colNum=dms[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)