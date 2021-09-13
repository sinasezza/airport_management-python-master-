from abc import ABC ,abstractclassmethod

class Airplane(ABC):

    #default constructor:
    def __init__(self) -> None:
        self.__IdentityCode = None;
    
    def SetIdentityCode(self,ID):
        self.__IdentityCode = ID;
    
    def GetIdentityCode(self):
        return self.__IdentityCode;

    @abstractclassmethod
    def SetCapacity(self):
        pass;
    
    @abstractclassmethod
    def GetCapacity(self):
        pass;

    def PrintInfo(self):
        print('{:<15}'.format('Identity Code'),'{:<5}'.format(':'),self.__IdentityCode);

