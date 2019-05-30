inp=input('nhap: ')

count_alpha=0
count_number=0

for letter in inp:
    count_alpha+=letter.isalpha()
    count_number+=letter.isnumeric()

print('so chu cai: %d'%count_alpha,'so chu so: %d'%count_number,sep='\n')