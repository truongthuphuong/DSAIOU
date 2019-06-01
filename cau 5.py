class InOutString(object):
   def __init__(self):
       self.s = ""

   def getString(self):
       self.s = input("Nhập chuỗi:")

   def printString(self):
       print (self.s.upper())

s = InputOutString()
s.getString()
s.printString()