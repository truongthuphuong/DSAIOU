# Chương trình xây dựng 1 class
# Nhận chuỗi và xuất ra chuỗi in hoa do người dùng nhập vào


class chuoi_in_hoa(object):
    s = ''

    # thuộc tính đối tượng chuỗi
    def __init__(self):
        self.s

    # phương thức
    def get_string(self):
        self.s = input("Nhap vao chuoi: ")

    def print_string(self):
        print(self.s.upper())


string = chuoi_in_hoa()
string.get_string()
string.print_string()
