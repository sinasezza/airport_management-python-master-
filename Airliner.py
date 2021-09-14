from Airplane import Airplane;

class Airliner(Airplane):
    
    #default constructor:
    def __init__(self,id,capacity) -> None:
        super().__init__(id)
        self.__Capacity = capacity;
    # --------------------------------------
   
    def SetCapacity(self,cap):
        self.__Capacity = cap;
    # --------------------------------------
    def GetCapacity(self):
        return self.__Capacity;
    # --------------------------------------
    def PrintInfo(self):
        Airplane.PrintInfo(self);
        print('{:<25}'.format('Capacity'),'{:<5}'.format(':'),self.__Capacity,'Person');