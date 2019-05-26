X=int(input('nhap X: '))
Y=int(input('nhap Y: '))

result_list=[]

for i in range(X):
    tmp_lst=[]
    for j in range(Y):
        tmp_lst.append(i*j)
    result_list.append(tmp_lst)

print(result_list)