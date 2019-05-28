class MyClass(object):
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("mời bạn nhập vào một chuỗi: ")
    def printString(self):
        print(self.s.upper())
strMC = MyClass()
strMC.getString()
strMC.printString()
