number=int(input("Nhập số vào đi em: "))
dict1= {}


def tudien(x):
    for i in range(1, x+1):
        dict1[i]=i*i
    return dict1

print ("Ra rồi mà chậm:",tudien(number))
