result=list()

for number in range(2000,3201):
    if (number%7==0) and not(number%5==0):
        result.append(str(number))

print(','.join(result))