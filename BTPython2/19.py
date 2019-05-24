values = input("Nhập 1 dãy số và cách nhau bằng 1 dấu phẩy: ")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))