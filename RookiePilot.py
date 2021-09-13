from Pilot import Pilot;

class RookiePilot(Pilot):

    #default initializer
    def __init__(self) -> None:
        super().__init__()
        self.__NumberOfFlights = None;
    # ----------------------------------
    @classmethod
    def RookiePilot_main_Constructor(self,lname,id,age):
        BuildClass = RookiePilot();
        BuildClass.LastName = lname;
        BuildClass.IdentityCode = id;
        BuildClass.Age=age;
        return BuildClass;
    # ----------------------------------
        
    def GetProfessionalDegree(self):
        raise NotImplemented;
    
    def SetProfessionalDegree(self,something):
        raise NotImplemented;

    # ----------------------------------
    def GetNumberOfFlights(self):
        return self.__NumberOfFlights;

    def SetNumberOfFlights(self,something):
        self.__NumberOfFlights = something;
    # ----------------------------------
    def PrintInfo(self):
        Pilot.PrintInfo(self);
        print('{:<25}'.format('Number OF Flights'),'{:<5}'.format(':'),self.__NumberOfFlights);