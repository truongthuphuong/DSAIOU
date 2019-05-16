class ng:
 name = "ng"
 def __init__(self, name = None):
 self.name = name

jeffrey = ng("Jeffrey")
print ("%s name is %s" % (ng.name, jeffrey.name))

nico = ng()
nico.name = "Nico"
print ("%s name is %s" % (ng.name, nico.name))