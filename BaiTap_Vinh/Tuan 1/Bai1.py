# Chương trình tìm các số chia hết cho 7 nhưng không phải là bội của 5
# Nằm trong khoảng 2000 đến 3200
numbers = []


for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(str(i))

print(','.join(numbers))
