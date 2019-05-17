class Inchuoi():

    def __init__(self):
        self.s=""

    def setstring(self):
        self.s=(input("Mời bạn nhập vào chuỗi: "))

    def getstring(self):
        return self.s
    def printstring(self):
        print(self.s.upper())

string= Inchuoi()
string.setstring()
string.getstring()
string.printstring()
