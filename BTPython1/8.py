class Ten:
    name = " Ten "
def __init__(self, name = None):
    self.name = name

    bang = Ten(" Băng")

    print(" Băng là tên" % (Ten.name, bang.name))

    tuyet = Ten()
    tuyet.name = " Tuyết "
    print(" Tuyết là tên lót" % (Ten.name, tuyet.name))




