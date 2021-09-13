from Airplane import Airplane;

class CargoPlane(Airplane):
    
    #default constructor:
    def __init__(self) -> None:
        super().__init__();
        self.__Capacity = None;
    # ------------------------------
    @classmethod
    def CargoPlane_main_Constructor(self,id,cap):
        BuildClass = CargoPlane();
        BuildClass.IdentityCode=id;
        BuildClass.SetCapacity(cap);
        return BuildClass;
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
