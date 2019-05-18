class Person:
    name = 'Person'

    def __init__(self, name = None):
        self.name = name


mary = Person('Mary')
print("%s name is %s" % (Person.name, mary.name))

nico = Person()
nico.name = 'Nico'
print("%s name is %s" % (Person.name, nico.name))
