import msvcrt;
from os import  system, name;
from time import sleep;
import sys
from AirportManager import AirportManager;

class UserMenu:
    def __init__(self) -> None:
        self.__airportmanager = AirportManager();
        self.MenuManager();
    
    # ------------------------------------------------------
    def ShowMenu(self):
        print(" *****************************************************");
        print(" *****************************************************");
        print("***************((AIRPORT MANAGEMENT))*******************");    
        print(" *****************************************************");
        print(" *****************************************************");
    #starting menu:
        print("please enter a number:\n");
        print("{:<60}".format("ADDING      AIRPLANE"),"press : 1");
        print("{:<60}".format("DELETING    AIRPLANE"),"press : 2");
        print("{:<60}".format("ADDING      FLIGHT"),"press : 3");
        print("{:<60}".format("DELETING    FLIGHT"),"press : 4");
        print("{:<60}".format("ADDING      PILOT"),"press : 5");
        print("{:<60}".format("DELETING    PILOT"),"press : 6");
        print("{:<60}".format("SHOWING ALL FLIGHTS REPORT"),"press : 7");
        print("{:<60}".format("SHOWING ALL AIRPLANES REPORT"),"press : 8");
        print("{:<60}".format("SHOWING ALL PILOTS"),"press : 9");
        print("{:<60}".format("EXIT PROGRAM"),"press : 0");
    # ------------------------------------------------------
    def MenuManager(self):
        self.ShowLoadingTitle();
        option = None;
        while(True):
            self.Clear();
            self.ShowMenu();
            option=self.GetOptionFromUser();

            if(  option == 0):
                self.Exit();
            elif(option == 1):
                self.__airportmanager.AddAirplane();
            elif(option == 2):   
                self.__airportmanager.DeleteAriplane();
            elif(option == 3):
                self.__airportmanager.AddFlight();
            elif(option == 4):
                self.__airportmanager.DeleteFlight();         
            elif(option == 5):
                self.__airportmanager.AddPilot();
            elif(option == 6):
                self.__airportmanager.DeletePilot();
            elif(option == 7):
                self.ShowAllFlightsReport();
            elif(option == 8):
                self.ShowAllAirplanesReport();
            elif(option == 9):
                self.ShowAllPilotsReport();
            else:
                self.Clear();
                print("wrong option inserted\n");
                print("press enter to continue...");
                msvcrt.getwch();
                #ShowMenu();
            self.StateFunc();
    # ------------------------------------------------------
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
    def GetOptionFromUser(self):
        # _ = msvcrt.getwch()
        # print(_ ,"is from type : ",type(_));
        # return int(_);
        return int(msvcrt.getwch());
    # ------------------------------------------------------
    def Exit(self):                                 
        if(self.Confirm("exit")):
            print("*******<<goodbye>>************************************");
            print("***************<<goodbye>>****************************");
            print("***********************<<goodbye>>********************");
            print("*******************************<<goodbye>>************");
            print("press any key to continue...");
            msvcrt.getwch();
            self.Clear();
            sys.exit();
    # ------------------------------------------------------
    def Confirm(self,title):                   
        self.Clear();
        print("are you sure to  ",title," ? [y,n]");
        while True:
            T=str(msvcrt.getwch());
            if(T.lower()=='y'):
                flag=True;
                self.Clear();
                return flag;
            elif (T.lower()=='n'):
                flag=False;
                self.Clear();
                return flag;
            print("wrong option entered \nplease enter [y,n]") 
    # ------------------------------------------------------
    def StateFunc(self):                            
        print("\n\nnote::\tfor return press: [r] \tfor exit press: [e]")
        state=str(msvcrt.getwch());
        if(state=='r'):
            return;
        else:
            if(state=='e'):
                self.Exit();
    # ------------------------------------------------------
    def ShowAllFlightsReport(self):
        self.Clear();
        if(len(self.__airportmanager.flight) == 0):
            print("there is not any flight yet...");
        else:
            print("\t\t\t<Flights>");
            for flight in self.__airportmanager.flight:
                flight.PrintInfo();
                self.PrintLine('*');
    # ------------------------------------------------------
    def ShowAllAirplanesReport(self):
        self.Clear();
        if(len(self.__airportmanager.airplane) == 0):
            print("there is not any airplane yet...");
        else:
            print("\t\t\t<Airliners>");
            for airplane in self.__airportmanager.airplane:
                if((type(airplane).__name__) == 'Airliner'):
                    airplane.PrintInfo();
                    self.PrintLine('*');

            self.PrintLine('=');
            self.PrintLine('=');

            print("\t\t\t<CargoPlanes>");
            for airplane in self.__airportmanager.airplane:
                if((type(airplane).__name__) == 'CargoPlane'):
                    airplane.PrintInfo();
                    self.PrintLine('*');
    # ------------------------------------------------------
    def ShowAllPilotsReport(self):
        self.Clear();
        if(len(self.__airportmanager.pilot) == 0):
            print("there is not any pilot yet...");
        else:
            print("\t\t\t<Rookie Pilots>");
            for pilot in self.__airportmanager.pilot:
                if((type(pilot).__name__) == 'RookiePilot'):
                    pilot.PrintInfo();
                    self.PrintLine('*');

            self.PrintLine('=');
            self.PrintLine('=');

            print("\t\t\t<Professional Pilots>");
            for pilot in self.__airportmanager.pilot:
                if((type(pilot).__name__) == 'ProfessionalPilot'):
                    pilot.PrintInfo();
                    self.PrintLine('*');
    # ------------------------------------------------------
    @staticmethod
    def ShowLoadingTitle():
        mylist = [];
        for i in range(51):
            UserMenu.Clear();
            print("{:>40}".format("<LOADING>"),"\t\t",i*2,"%\n")
            print('|'*i,end='');
            print('',end=None);
            sleep(0.02);  
        print("{:>35}".format("LOADED...\t\tPlease wait"));
        sleep(2.5);  