from abc import ABC ,abstractclassmethod

class Airplane(ABC):

    #default constructor:
    def __init__(self,id) -> None:
        self.__IdentityCode = id;
    # -----------------------------
    @property
    def IdentityCode(self):
        return self.__IdentityCode;
    @IdentityCode.setter
    def IdentityCode(self,ID):
        self.__IdentityCode = ID;
    # -----------------------------

    @abstractclassmethod
    def SetCapacity(self):
        pass;
    # -----------------------------
    @abstractclassmethod
    def GetCapacity(self):
        pass;
    # -----------------------------
    def PrintInfo(self):
        print('{:<25}'.format('Identity Code'),'{:<5}'.format(':'),self.__IdentityCode);

