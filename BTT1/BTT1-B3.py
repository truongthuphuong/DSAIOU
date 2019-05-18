# Tạo dictionary

n = int(input("Nhập n: "))
dictionary = dict()
for i in range(1, n+1):
    dictionary[i] = i*i
print(dictionary)
