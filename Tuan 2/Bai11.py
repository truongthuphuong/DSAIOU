# Chương trình nhập vào 1 chuỗi mỗi từ cách nhau dấu phẩy
# xuất ra lại những từ đó và sắp xếp theo chữ cái

s = input("Nhap vao cac tu cach nhau dau phay: ")
words = s.split(",")
words.sort()
print(",".join(words))
