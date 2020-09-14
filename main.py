import PortScanner
from os import system
print("     1======> [ $$PortScanner$$ ]\n")
choice=input("Enter Your Choice(1/2/3/4) : ")
if ( choice == "1" ) :
    ''' Part1 : 
             PortScanner 
                         '''
    system("clear") 
    print("[1]Scan All Ports[1]\n")
    print("[2]Scan a Specific Port[2]\n")
    choise=input("Enter Your Choice(1/2/3/4) : ")
    if choise=="1" :
        host=input("Enter Target Host :\n")
        PortScanner.ScanAllPorts(host)
    elif choise=="2" :
        system("clear")
        host=input("Enter Traget Host :\n")
        port=int(input("Enter Target Port :\n"))
        PortScanner.ScanPort(host,port)
