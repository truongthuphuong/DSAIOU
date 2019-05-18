# Định nghĩa class

class KiemTraInHoa(object):

	def __init__(self):
		self.str = ""

	def get_string(self):
		self.str = input("Mời bạn nhập chuỗi: ")

	def prin_tsring(self):
		print("Chuỗi bạn vừa nhập:", self.str.upper())


strobj = KiemTraInHoa()
strobj.getstring()
strobj.printsring()
