class Person:
 name = "Person"
 def __init__(self, name = None):
    self.name = name
chau = Person("Châu")
print ("%s name is %s" % (Person.name, chau.name))

minh = Person()
minh.name = "Minh"
print ("%s name is %s" % (Person.name, minh.name))