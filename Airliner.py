from Airplane import Airplane;

class Airliner(Airplane):
    
    #default constructor:
    def __init__(self) -> None:
        super().__init__()
        self.__Capacity = None;
    
    @classmethod
    def Airliner_main_Constructor(self,id,capacity):
        BuiltClass = Airliner();
        BuiltClass.SetIdentityCode(id);
        BuiltClass.SetCapacity(capacity)
        return BuiltClass;
   
    def SetCapacity(self,cap):
        self.__Capacity = cap;
    
    def GetCapacity(self):
        return self.__Capacity;

    def PrintInfo(self):
        Airplane.PrintInfo(self);
        print('{:<15}'.format('Capacity'),'{:<5}'.format(':'),self.__Capacity,'Person');