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

    ownbool = False
    while(ownbool == False):
        #section for checking if new sin is entered
        owner_id = input("please provide owner's sin")
        search_str = ("SELECT name FROM people WHERE p.sin =",owner_id,";")
        curs.execute(search_str)    
        result = curs.fetchall()
        if (result.len() == 0):
            n_own = 'y'
            n_own = input("new sin entered, add new person? (y) or (n) or (e) >")
            if (own == 'e'):
                pass            
        else:  
            n_own = input("user found, add vehicle? (y)es or (n)o or (e)xit >")
            if (own == 'e'):
                pass        
            
            
        if (n_own == 'y'):
            #to be done
            name = str(input("provide person's name"))
            height = input("provide height")
            weight = int(input("provide weight (lbs)"))
            eyecolor = input("provide eye color")
            haircolor = input("provide haircolor")
            addr = input("provide address")
            gender = input("provide gender")
            birthday = input("provide birthday")
            pdata = [(owner_id,name,height,weight,eyecolor,haircolor,addr,gender,birthday)]
            cursInsert.bindarraysize = 1
            cursInsert.setinputsizes(30, 30, int, int, 10, 10, 30, 50, 1, DATE)
            cursInsert.executemany("INSERT INTO people(owner_id,name, height, weight, eyecolor, haircolor, addr, gender, birthday)" 
                                   "VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)",pdata)               
            own = 'n'
            
            #new owner handled, vehicle adding
        if (n_own == 'n'):
            
            serial_no = input("inpur serial_no")
            maker = input("input maker >")
            model = input("input model >")
            year = input("input year >")
            color = input("input color >")
            type_id = input("input type_id >")
            vdata = [(serial_no, maker, model, year, color, type_id)]            
            
            
            cursInsert.bindarraysize = 1
            cursInsert.setinputsizes(int, 30, 30, int, 15, int)
            cursInsert.executemany("INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)" 
                                   "VALUES (:1, :2, :3, :4, :5, :6)",vdata)
            
            primary_owner = input("is he/she primary owner of this vehicle? ")
            odata = [(owner_id,serial_no,is_primary_owner)]            
            
            cursInsert.bindarraysize = 1
            cursInsert.setinputsizes(int, int, bool)
            cursInsert.executemany("INSERT INTO owner(owner_id,vehicle_id,is_primary_owner)" 
                                   "VALUES (:1, :2, :3)",odata)   
        
        else:
            own = input("enter another owner/vehicle? (y) or (n) or (e) to exit> ").lower()
            if (own == 'e'):
                ownbool = True
            if (own == 'n'):
                ownbool = True
                


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
