
class Flight():
    # default constructor
    def __init__(self,origin,destination,airplane_id,pilot_id) -> None:
        self.__Origin = origin;
        self.__Destination = destination;
        self.__AirplaneIdentityCode = airplane_id;
        self.__PilotIdentityCode=pilot_id;
    
    # -------------------------------------------      
    @property
    def Origin(self):
        return self.__Origin;
    @Origin.setter
    def Origin(self,somename):
        self.__Origin = somename;
    # -------------------------------------------
    @property
    def Destination(self):
        return self.__Destination;
    @Destination.setter
    def Destination(self,someDestination):
        self.__Destination = someDestination;
    # -------------------------------------------
    @property
    def AirPlaneIdentityCode(self):
        return self.__AirplaneIdentityCode;
    @AirPlaneIdentityCode.setter
    def AirPlaneIdentityCode(self,soemid):
        self.__AirplaneIdentityCode = soemid;
    # -------------------------------------------
    @property
    def PilotIdentityCode(self):
        return self.__PilotIdentityCode;
    @PilotIdentityCode.setter
    def PilotIdentityCode(self,someid):
        self.__PilotIdentityCode = someid
    # -------------------------------------------
    def PrintInfo(self):
        print('{:<25}'.format('Origin'),'{:<5}'.format(':'),self.Origin);
        print('{:<25}'.format('Destination'),'{:<5}'.format(':'),self.Destination);
        print('{:<25}'.format('Airplane Identity Code'),'{:<5}'.format(':'),self.AirPlaneIdentityCode);
        print('{:<25}'.format('Pilot Identity Code'),'{:<5}'.format(':'),self.PilotIdentityCode);