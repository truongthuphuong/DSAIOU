# Định nghĩa tham số lớp và có cùng tham số instance
class xe_hoi(object):
    name = 'Xe oto'

    def __init__(self, name=None):
        self.name = name


honda = xe_hoi()
honda.name = "Honda"
print("{0} ten la {1}".format(xe_hoi.name, honda.name))
