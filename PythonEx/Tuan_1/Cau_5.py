class UpperCaseString:
    def __init__(self):
        self.__String=None

    def getString(self,string=None):
        self.__String=string
    
    def __isEmpty(self):
        if self.__String==None or self.__String=='':
            return True
        else:
            return False  

    def printString(self):
        if self.__isEmpty():
            print("__ERROR! EMPTY STRING!__")
        else:
            print(self.__String.upper())

if __name__ == "__main__":
    String=input('input:')
    upperString=UpperCaseString()
    upperString.getString(String)
    upperString.printString()
        
