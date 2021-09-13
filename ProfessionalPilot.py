from Pilot import Pilot;

class ProfessionalPilot(Pilot):
    
    #default initializer
    def __init__(self) -> None:
        super().__init__()
        self.__ProfessionalDegree = None;
    # ----------------------------------
    @classmethod
    def ProfessionalPilot_main_Constructor(self,lname,id,age):
        BuildClass = ProfessionalPilot();
        BuildClass.LastName = lname;
        BuildClass.IdentityCode = id;
        BuildClass.Age=age;
        return BuildClass;
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
        print('{:<25}'.format('Professional Degreee'),'{:<5}'.format(':'),self.__ProfessionalDegree);