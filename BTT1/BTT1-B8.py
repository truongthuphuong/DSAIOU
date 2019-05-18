# Định nghĩa class có tham số class và có cùng tham số instance


class Person:

    def __init__(self, name=None):
        # self.name là biến instance
        self.name = name
        self.salary = salary

    def print(self):
        print(self.name)
        print(self.salary)


a = Person(input("Nhập tên: "), int(input("Nhập lương: ")))
print(a.name)
print(a.salary)

