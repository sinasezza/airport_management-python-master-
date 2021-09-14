from Pilot import Pilot;

class ProfessionalPilot(Pilot):
    
    #default initializer
    def __init__(self,Lname,id,age,ProDegree) -> None:
        super().__init__(Lname,id,age)
        self.__ProfessionalDegree = ProDegree;
    
    # ----------------------------------
    def GetProfessionalDegree(self):
        return self.__ProfessionalDegree;
    
    def SetProfessionalDegree(self,something):
        self.__ProfessionalDegree = something;
        
    # ----------------------------------
    def GetNumberOfFlights(self):
        raise NotImplemented;

    def SetNumberOfFlights(self,something):
        raise NotImplemented;
    # ----------------------------------
    def PrintInfo(self):
        Pilot.PrintInfo(self);
        print('{:<25}'.format('Professional Degree'),'{:<5}'.format(':'),self.__ProfessionalDegree);