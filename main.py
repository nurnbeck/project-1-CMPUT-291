#DATABASE MAIN
#default

import sys
import cx_Oracle
import getpass
from searchEngine import searchEngine              # ############# modification 2015.Mar.15 ############## 
from setup import setup_tbls
from datetime import date, datetime, timedelta

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
        connstr = input("Enter your username: ")
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


def newVehicleRegistration(curs,connection):
    #curs.execute()
    #enter car data to be inserted(will refine later)
    #error handling will be done later
    
    ownbool = False
    while(ownbool == False):
        #section for checking if new sin is entered
        owner_id = str(input("please provide owner's sin > "))
        search_str = "SELECT name FROM people p WHERE p.sin = \'"
        search_str += owner_id
        search_str +=  "\'"
        print(search_str)
        curs.execute(search_str)
        result = curs.fetchall()
        if (len(result) == 0):
            n_own = 'y'
            n_own = input("new sin entered, add new person? (y)es or (n)o or (e)xit >")
            if (n_own == 'e'):
                pass            
        else:  
            n_own = input("user found, add vehicle? (y)es or (n)o or (e)xit >")
            if (n_own == 'n'):
                n_own = 'e'
            if (n_own == 'e'):
                pass        
            
            
        if (n_own == 'y'):
            #to be done
            name = str(input("provide person's name > "))
            height = input("provide height > ")
            weight = int(input("provide weight (lbs) > "))
            eyecolor = input("provide eye color > ")
            haircolor = input("provide haircolor > ")
            addr = input("provide address > ")
            gender = input("provide gender m or f > ")
            
            birthday = input("provide birthday in y(xxxx) m(xx) day(xx) format > ")
            #FIX DATE OF BIRTH BUG
            birthdayarr = birthday.split(' ')
            while((len(birthdayarr) > 2) or (int(birthdayarr[1]) > 12)):
                birthday = input("provide proper birthday format > yxxxx mxxxx dxx ")
                birthdayarr = birthday.split(' ')
            year = int(birthdayarr[0])
            month = int(birthdayarr[1])
            if (int(birthdayarr[2]) > 31):
                birthdayarr[2] = input("please input day in range 1-31")
            day = int(birthdayarr[2])
            print(year)
            birthday = date(year,month,day)
            pdata = [(owner_id,name,height,weight,eyecolor,haircolor,addr,gender,birthday)]
            #curs.bindarraysize = 1
            #curs.setinputsizes(30, 30, int, int, 10, 10, 30, 50, 1, cx_0racle.Date)
            #curs.execute("INSERT INTO people(owner_id,name, height, weight, eyecolor, haircolor, addr, gender, birthday)" 
            #                       "VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)",pdata)               
            curs.execute("INSERT INTO people(owner_id,name,height,weight,eyecolor,haircolor,addr,gender,birthday)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, '%s') ",(owner_id,name,height,weight,eyecolor,haircolor,addr,gender,birthday))
            
            
            
            
            n_own = 'n'
            
            #new owner handled, vehicle adding
        if (n_own == 'n'):
            
            serial_no = input("inpur serial_no > ")
            maker = input("input maker > ")
            model = input("input model > ")
            year = input("input year > ")
            color = input("input color > ")
            type_id = input("input type_id > ")
            vdata = [(serial_no, maker, model, year, color, type_id)]            
            
            
            cursInsert.bindarraysize = 1
            cursInsert.setinputsizes(int, 30, 30, int, 15, int)
            cursInsert.executemany("INSERT INTO vehicle(serial_no, maker, model, year, color, type_id)" 
                                   "VALUES (:1, :2, :3, :4, :5, :6)",vdata)
            
            primary_owner = input("is he/she primary owner of this vehicle? ")
            odata = [(owner_id,serial_no,is_primary_owner)]            
            
            curs.bindarraysize = 1
            curs.setinputsizes(int, int, bool)
            curs.executemany("INSERT INTO owner(owner_id,vehicle_id,is_primary_owner)" 
                                   "VALUES (:1, :2, :3)",odata)   
        
        else:
            own = input("enter another owner/vehicle? (y) or (n) or (e) to exit> ").lower()
            if (own == 'e'):
                ownbool = True
            if (own == 'n'):
                ownbool = True
                


def autoTransaction():
    pass


def driverLicenceRegistration(curs, connection):
    sin = str(input("please input user sin > "))
    search_str = 'SELECT name FROM people p WHERE p.sin =\''
    search_str += sin
    search_str += "\'"
    print(search_str)
    curs.execute(search_str)    
    result = curs.fetchall()
    if (len(result) == 0):
        n_own = 'y'
        #n_own = input("new sin entered, add new person? (y) or (n) or (e) > ")
        if (n_own == 'e'):
            pass
        else:  
            n_own = input("user found, add vehicle? (y)es or (n)o or (e)xit > ")
            if (n_own == 'e'):
                pass            
    licence_no = input("input licence number > ")
    Dclass = input("input licence class > ")
    photo = input("input (photoname).jpg > ")
    issuing_date = input("input issuing date > ")
    expiring_date = input("input expiration date > ")
    
    
    f_image  = open(photo,'rb')
    photo  = f_image.read()
    ddata =(licence_no, sin, Dclass, photo, issuing_date, expiring_date)

    #prepare memory for operation parameters
    curs.bindarraysize = 1
    curs.setinputsizes(30, 30, 10 , cx_Oracle.BLOB, cx_0racle.Date, cx_0racle.Date)
    curs.setinputsizes(photo = cx_Oracle.BLOB)
    cursInsert.executemany("INSERT INTO drive_license( licence_no, sin, class, photo, issuing_date, expiring_date)" 
                                       "VALUES (:1, :2, :3, :4, :5, :6)",ddata)    
    
    insert = """insert into drive_license( licence_no, sin, class, photo, issuing_date, expiring_date)
    values (:license_no, :sin, :class, :image, :issuing_date, expiring_date)"""
    curs.execute(insert,{'licence_no':licence_no, 'sin':sin,
                           'Dclass':Class, 'photo':image, 'issuing_date':issuing_date, 'expiring_date':expiring_date})
    

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
    setup_tbls(curs, connection)

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
            newVehicleRegistration(curs, connection)
        elif inp == '2' or inp == 'a':
            autoTransaction()
        elif inp == '3' or inp == 'd':
            driverLicenceRegistration(curs, connection)
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
