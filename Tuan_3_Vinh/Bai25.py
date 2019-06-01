# Chương trình in ra màn hình tần suất xuất hiện của 1 chữ or số
# Sắp xếp theo bảng chữ cái
s = input("Nhap vao chuoi: ")
list_str = s.split(" ")
tan_so_tu = {}


for word in list_str[:]:
    if word in tan_so_tu:
        tan_so_tu[word] += 1
    else:
        tan_so_tu[word] = 1

words = sorted(tan_so_tu.keys())

for w in words:
    print("{0}:{1}".format(w, tan_so_tu[w]))
