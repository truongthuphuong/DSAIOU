
result=[]
for i in range(1000,3000):
    s=str(i)
    if(int(s[0])%2==0):
        if (int(s[1])%2==0):
            if(int(s[3])%2==0):
                result.append(s)
print(','.join(result))