result=[]
for num in range(2000,3001):
    isEven=True
    cur_num=num
    while isEven:
        if cur_num==0:
            break
        else:
            isEven=not(bool((cur_num%10)%2))
            cur_num=cur_num//10
    if isEven:
        result.append(str(num))

print(','.join(result))