from Pilot import Pilot;

class RookiePilot(Pilot):

    #default initializer
    def __init__(self,Lname,id,age,FlightNum) -> None:
        super().__init__(Lname,id,age)
        self.__NumberOfFlights = FlightNum;
   
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