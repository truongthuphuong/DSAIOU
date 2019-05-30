str_input=input('nhap: ').split(',')
List_number=[int(x) for x in str_input]

list_odd=[]

for num in List_number:
    if num % 2 != 0:
        list_odd.append(str(num))

print(','.join(list_odd))