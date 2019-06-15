# CAU1
KQ = []
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        KQ.append(str(i))
print('-'.join(KQ))
#CAU2
x = input("Nhập vào số cần tính giai thừa:")
def giaithua (x):
    if x == 0:
        return 1
    return x*giaithua(x-1)
print (giaithua(x))
#CAU3
x = int(input("Nhập vào số cần tính:")
dictionary = dict()
for i in range (1, x+1):
    dictionary[i]=i*i
print(dictionary)
#CAU4
s=input("Nhập vào các giá trị cần tính:")
l=s.split(",")
t=tuple(l)
print (l)
print (t)
#CAU5
class In_Hoa():
    def __init__(self):
        self.str = ""
    def get_String(self):
        self.str = input("Nhap vao mot chuoi ky tu: ")
    def print_String(self):
        print(self.str.upper())

myStr = In_Hoa()
myStr.__init__()
myStr.get_String()
myStr.print_String()
#CAU6
x = input("Nhập vào giá trị cần tính:")
def square(num):
  return num ** 2
print (square(x))
#CAU7


