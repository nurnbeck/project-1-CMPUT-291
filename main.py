#DATABASE MAIN
#default

import sys
import cx_Oracle
import getpass
from searchEngine import searchEngine              # ############# modification 2015.Mar.15 ############## 

def connect():
    '''
    connstr = input("Enter your user name: ")
    connstr += '/' + getpass.getpass("Enter your password: ")
    connstr += '@gwynne.cs.ualberta.ca:1521/crs'
    try:
        print("Connection successful")
        connection = cx_Oracle.connect(connstr)
    except cx_Oracle.DatabaseError as exc:
        print("Unable to connect to database")
        error, = exc.args
        print(sys.stderr, "Oracle code:". error.code)
        print(sys.stderr, "Oracle message:", error.message)
    return connection, connection.cursor()
    '''
    logintime = 0
    while logintime < 3:
        connstr = input("Enter youe username: ")
        if connstr.lower() == 'q' or connstr.lower() == "quit":
            return 0, 0
        connstr += '/' + getpass.getpass("Enter your password: ")
        connstr += '@gwynne.cs.ualberta.ca:1521/crs'
        try:
            connection = cx_Oracle.connect(connstr)
            print("Connection successful")
            return connection, connection.cursor()
        except:
            print("Unable to connect to the database")
            logintime += 1
            continue
    print("Unable to connect to ORACLE after 3 attempts, exit the program")
    return 0, 0


def newVehicleRegistration():
    #curs.execute()
    #enter car data to be inserted(will refine later)
    #error handling will be done later
    serial_no = input("inpur serial_no")
    maker = input("input maker >")
    model = input("input model >")
    year = input("input year >")
    color = input("input color >")
    type_id = input("input type_id >")
    vdata = [(serial_no, maker, model, year, color, type_id)]
    
    own = input("new vehicle owner? (y) or (n) > ").lower()
    ownbool = False
    while(ownbool == FALSE):
        if (own == 'y'):
            #to be done
            ownbool = TRUE
            pass
        if (own == 'n'):
            owner_id = input("please provide owner's sin")
            prime_o = input("is he/she primary owner? ")
            odata = [(owner_id,serial_no,is_primary_owner)]
             
            cursInsert = connection.cursor()
            cursInsert.bindarraysize = 1
            cursInsert.setinputsizes(int, int, bool)
            cursInsert.executemany("INSERT INTO owner(owner_id,vehicle_id,is_primary_owner)" 
                                   "VALUES (:1, :2, :3)",odata)   
            
            cursInsert = connection.cursor()
            cursInsert.bindarraysize = 1
            cursInsert.setinputsizes(int, 30, 30, int, 15, int)
            cursInsert.executemany("INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)" 
                                   "VALUES (:1, :2, :3, :4, :5, :6)",vdata)   
            ownbool = TRUE
            pass
        else:
            print("please provide proper response or (e) to exit")
            own = input("new vehicle owner? (y) or (n) or (e) to exit> ")
            if (own = e):
                pass
    pass


def autoTransaction():
    pass


def driverLicenceRegistration():
    pass


def violationRecord():
    pass

'''
def searchEngine(curs, connection): # ############# modification 2015.Mar.15 ##############
    pass
'''

# will call setup function somewhere in the main function
def main():
    connection, curs = connect()
    if connection == 0:
        print("Bye")
        return
    
    # setup new tables
    setup(curs, connection)

    print("1. New Vehicle Registration (n)")
    print("2. Auto Transaction (a)")
    print("3. Driver Licence Registration (d)")
    print("4. Violation Record (v)")
    print("5. Search Engine (s)")

    while True:
        inp = input("Enter your choice: ").lower()
        if inp == 'q' or inp == 'quit' or inp == "exit":
            while True:
                inp = input("Do you want to exit? ").lower()
                if inp == 'y' or inp == 'yes' or inp == 'q':
                    print("Quit")
                    return
                elif inp == 'n' or inp == 'no':
                    break
                else:
                    print("Please enter yes (y) or no (n)")
                    continue
            continue
        elif inp == '1' or inp == 'n':
            newVehicleRegistration()
        elif inp == '2' or inp == 'a':
            autpTransaction()
        elif inp == '3' or inp == 'd':
            driverLicenceRegistration()
        elif inp == '4' or inp == 'v':
            violationRecord()
        elif inp == '5' or inp == 's':
            searchEngine(curs, connection)           # ############# modification 2015.Mar.15 ##############
        else:
            print("Invalid")
        print(inp)

    cursor.close()
    connection.close()
    return

if __name__ == "__main__":
    main()
