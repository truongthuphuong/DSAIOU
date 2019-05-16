class Person:
 name = "Person"
 def __init__(self, name = None):
    self.name = name
jerry = Person("Jerry")
print ("%s name is %s" % (Person.name, jerry.name))

thomas = Person()
thomas.name = "Thomas"
print ("%s name is %s" % (Person.name, thomas.name))
