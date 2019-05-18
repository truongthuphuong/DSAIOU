
j = [] #tạo list
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i)) #cập nhật chuỗi i vào list j
print(",".join(j))

