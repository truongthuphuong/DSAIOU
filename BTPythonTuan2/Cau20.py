d = []
w = []
sum_d = 0
sum_w = 0
while True:
    s = input().split(' ')
    if s[0] == 'D':
        d.append(s[1])
    elif s[0] == 'W':
        w.append(s[1])
    else:
        break
def sum(d, sum_d):
    for i in range(len(d)):
        d[i] = int(d[i])
        sum_d += d[i]
    return sum_d
print(sum(d, sum_d) - sum(w, sum_w))

