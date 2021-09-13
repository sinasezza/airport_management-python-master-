from abc import ABC,abstractclassmethod;

class Pilot(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__LastName = None;
        self.__Age = None;
        self.__IdentityCode = None

    @property
    def IdentityCode(self):
        return self.__IdentityCode;
    @IdentityCode.setter
    def IdentityCode(self,ID):
        self.__IdentityCode = ID;
    
    @property
    def Age(self):
        return self.__Age;
    @Age.setter
    def Age(self,age):
        self.__Age = age;
    
    @property
    def LastName(self):
        return self.__LastName;
    @LastName.setter
    def LastName(self,lname):
        self.__LastName= lname;

    @abstractclassmethod
    def GetProfessionalDegree(self):
        pass;
    @abstractclassmethod
    def SetProfessionalDegree(self,something):
        pass;

    @abstractclassmethod
    def SetNumberOfFlights(self,something):
        pass;
    @abstractclassmethod
    def GetNumberOfFlights(self):
        pass;

    def PrintInfo(self):
        print('{:<25}'.format('Identity Code'),'{:<5}'.format(':'),self.__IdentityCode);
        print('{:<25}'.format('Last Name'),'{:<5}'.format(':'),self.__LastName);
        print('{:<25}'.format('Age'),'{:<5}'.format(':'),self.__Age);