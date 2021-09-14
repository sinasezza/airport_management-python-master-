from Airplane import Airplane;

class CargoPlane(Airplane):
    
    #default constructor:
    def __init__(self,id,cap) -> None:
        super().__init__(id);
        self.__Capacity = cap;

    # ------------------------------
    def SetCapacity(self,cap):
        self.__Capacity = cap;
    # ------------------------------
    def GetCapacity(self):
        return self.__Capacity;
    # ------------------------------
    def PrintInfo(self):
        Airplane.PrintInfo(self);
        print('{:<25}'.format('Capacity'),'{:<5}'.format(':'),self.__Capacity,'Ton(s)');