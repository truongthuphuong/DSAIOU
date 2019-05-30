import numpy as np
inp=input('nhap: ').split(',')
inp=np.array([int(n,base=2) for n in inp])

n=inp[np.where(inp%5==0)]
result=list(map(np.binary_repr,n))
print(','.join(result))