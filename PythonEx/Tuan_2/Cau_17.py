inp=input('nhap: ')

count_lower=0
count_upper=0

for letter in inp:
    count_lower+=letter.islower()
    count_upper+=letter.isupper()

print('chu thuong: %d'%count_lower,'so hoa: %d'%count_upper,sep='\n')