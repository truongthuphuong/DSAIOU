s = []
for i in range(2000, 3200):
    if(i % 5 != 0) and (i % 7 == 0):
        s.append(str(i))

print((s),)