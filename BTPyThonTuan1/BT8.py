class Name:
    name = "Ho"
def __init__(self, name = None):
    self.name= name

    Nguyen = Name("Nguyễn")
    print("Nguyễn là họ" % (Name.name, Nguyen.name))
    Anh=Name("Anh")
    print("Anh là tên:  " % (Name.name,Anh.name ))
