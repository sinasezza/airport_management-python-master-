from os import  remove, system, name;
import sys

from Flight import Flight;
from CargoPlane import CargoPlane;
from Airliner import Airliner;
from RookiePilot import RookiePilot;
from ProfessionalPilot import ProfessionalPilot;

class AirportManager:
    def __init__(self) -> None:
        self.__NumberOfAirplanes = 20;
        self.__NumberOFPilots =10;
        self.__NumberOFFlights = 8;
        self.flight =[];
        self.airplane =[];
        self.pilot =[];

    # ------------------------------------

    @staticmethod
    def Clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    # ------------------------------------------------------
    @staticmethod
    def PrintLine(entered_char='-'):
        print(entered_char*80);
    # ------------------------------------------------------
    def AddFlight(self):
        self.Clear();
        if( len(self.flight) >= self.__NumberOFFlights):
            print("We Reach the Maximum Number  of Flights...");
        else:
            origin = input("enter Origin : ");
            destination = input("enter destination : ");
            airplane_identity = input("enter Airplane Identity code : ");
            pilot_identity = input("enter Pilot Identity code : ");

            self.Clear();

            self.flight.append(Flight(origin,destination,airplane_identity,pilot_identity)) ;  
            print("\t\t<your Flight>");  
            self.flight[-1].PrintInfo();
    # ------------------------------------------------------     
    def DeleteFlight(self):
        self.Clear();
        Found = False;
        Airplane_ID =input("enter IdentityCode of Airplane : ");
        Pilot_ID = input("enter IdentityCode of Pilot : ");
        for flight in self.flight:
            if(flight.AirPlaneIdentityCode == Airplane_ID and 
                flight.PilotIdentityCode == Pilot_ID):
                Found = True
                print("your flight has been deleted");
                self.flight.remove(flight);
        if(not Found):
            print("Not Found ...:\\");
    # ------------------------------------------------------
    def AddAirplane(self):
        self.Clear();
        if( len(self.airplane) >= self.__NumberOfAirplanes):
            print("We Reach the Maximum Number  of Airplanes...");
        else:
            TypeNum = int(input("enter type of Airplane [1 for Cargo,2 for Airliner] : "));
            identity_code = input("enter IdentityCode of Airplane : ");
            if(TypeNum == 1):
                capacity = int(input("enter Maximum tolerable weight (capacity) : "));
                self.Clear();
                self.airplane.append(CargoPlane(identity_code,capacity));
                print("\t\t<your Airplane>");
                self.airplane[-1].PrintInfo();
            elif (TypeNum == 2):
                capacity = int(input("enter Maximum number of passangers (capacity) : "));
                self.Clear();
                self.airplane.append(Airliner(identity_code,capacity));
                print("\t\t<your Airplane>");
                self.airplane[-1].PrintInfo();
    # ------------------------------------------------------
    def DeleteAriplane(self):
        self.Clear();
        Found = False;
        identity_code = input("Enter Airplane's Identity Code : ");
        for airplane in self.airplane:
            if(airplane.IdentityCode == identity_code):
                Found = True;
                print("Deleted ...");
                self.airplane.remove(airplane);  
        if(not Found):
               print("Not Found ...:\\");
    # ------------------------------------------------------
    def AddPilot(self):
        self.Clear();
        if(len(self.pilot) >= self.__NumberOFPilots):
            print("We Reach the Maximum Number  of Pilots...");
        else:
            TypeNum = int(input("enter type of Pilot [1 for Rookie,2 for Professional] : "));
            identity_code = input("enter IdentityCode of Pilot : ");
            lastname = input("enter Last Name of Pilot : ");
            age = input("enter Age of Pilot : ");

            if(TypeNum == 1):
                flight_num = int(input("enter Number of Flights(since) : "));
                self.Clear();
                self.pilot.append(RookiePilot(lastname,identity_code,age,flight_num));
                print("\t\t<your Pilot>");
                self.pilot[-1].PrintInfo();
            elif(TypeNum == 2):
                degree = int(input("enter Professional Degree for professional pilot : "))
                self.Clear();
                self.pilot.append(ProfessionalPilot(lastname,identity_code,age,degree));
                print("\t\t<your Pilot>");
                self.pilot[-1].PrintInfo();
    # ------------------------------------------------------
    def DeletePilot(self):
        self.Clear();
        Found = False;
        identity_code = input("enter IdentityCode of Pilot : ");
        for pilot in self.pilot:
            if(pilot.IdentityCode == identity_code):
                Found = True;
                self.pilot.remove(pilot);
                print("Deleted ...");
        if(not Found):
            print("Not found ... :\\");
    # ------------------------------------------------------