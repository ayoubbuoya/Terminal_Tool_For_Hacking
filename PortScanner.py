import socket
from sys import exit
from datetime import datetime
def ScanAllPorts(host) :
    '''Scan All Ports From 0 To 10000'''
    #Check Time
    t1=datetime.now()
    try :
        for port in range(0,10000) :
            #Create Port
            s=socket.socket() 
            result=s.connect_ex((host,port))
            if ( result == 0) :
                print("Port {} ===>Opened".format(port))
            else :
                print("Port {} ===>Closed".format(port))
            s.close()
    except KeyboardInterrupt :
        print("Exiting...")
        exit()
    except socket.gaierror :
        print("Socket Name Can Not Resolved ")
        print("Exiting...")
        exit()
    except socket.error :
        print("Can't Connect")
        print("Exiting...")
        exit
    #Check Time Again
    t2=datetime.now()
    #Total Time
    tf=t2-t1
    print("\nScan All Ports In {} ".format(tf))
def ScanPort(host,port) :
    '''Function To Scan Only One Port '''
    s=socket.socket()
    port_service=socket.getservbyport(port)
    result=s.connect_ex((host,port)) 
    if result == 0 :
        print("Traget Port {}:{} ===> Opened".format(port,port_service))
    else :
        print("Target Port {}:{} ===> Closed".format(port,port_service))