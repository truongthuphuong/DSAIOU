class In_chuoi():
    def __init__(self):
        self.s = ""

    def set_string(self):
        self.s = str(input("moi nhap vao chuoi: "))

    def get_string(self):
        return self.s

    def print_string(self):
        print(self.s.upper())


string1 = In_chuoi()
string1.set_string()
string1.get_string()
string1.print_string()
