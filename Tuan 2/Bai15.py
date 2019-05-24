# In tất cả các số chẵn cách bởi dấu phẩy trong chuỗi 1000 => 3000
list_kq = []


def in_so_chan():
    for i in range(1000, 3001):
        i = str(i)
        if(int(i[0]) % 2 == 0 and int(i[0]) != 0 and
            int(i[1]) % 2 == 0 and int(i[1]) != 0 and
            int(i[2]) % 2 == 0 and int(i[2]) != 0 and
            int(i[3]) % 2 == 0 and int(i[3]) != 0):
            list_kq.append(i)


in_so_chan()
print(",".join(list_kq))
