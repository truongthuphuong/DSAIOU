class squared:
    def __init__(self,number=None):
        self.__number=number
    
    def __isEmpty(self):
        if self.__number==None:
            return True
        else:
            return False
    
    def printSquared(self):
        if self.__isEmpty():
            print("__ERROR! EMPTY !__")
        else:
            print('square of %d : '%self.__number,self.__number**2)

if __name__ == "__main__":
    number=int(input('input : '))
    numberSquared=squared(number)
    numberSquared.printSquared()
