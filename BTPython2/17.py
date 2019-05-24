s = input("Nhập câu của bạn: ")
d={"UPPER CASE":0, "LOWER CASE":0}
# Code by Quantrimang.com
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("Tổng số chữ in hoa trong câu là:", d["UPPER CASE"])
print ("Tổng số chữ thường trong câu là:", d["LOWER CASE"])