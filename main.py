#DATABASE MAIN
#default

import sys
import cx_Oracle
import getpass
import os
from datetime import date, datetime, timedelta

from VehicleReg import *
from autoTransaction import *
from driverlicenceregistration import *
from violationRecord import *
from searchEngine import *
from addvehicle import *

def connect():
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


'''
#New vehicle registration
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
            if (n_own == 'n'):
                return
            if (n_own == 'e'):
                return     
        else:  
            n_own = input("user found, add vehicle? (y)es or (n)o or (e)xit >").lower()
            while ((n_own != 'y') or (n_own != 'n')):
                if (n_own == 'n'):
                    return
                if (n_own == 'e'):
                    return    
                #confusing but just skips adding new people
                if (n_own == 'y'):
                    n_own = 'n'
                    break
                    
            
            
        if (n_own == 'y'):
            #adding new people
            addperson(curs, connection, owner_id)
            n_own = 'n'
            #new owner handled, vehicle adding
        if (n_own == 'n'):
            while(n_own == 'n'):
                vehicle_id = str(input("please provide vehicle serial number > "))
                search_str = "SELECT serial_no FROM vehicle v WHERE v.serial_no = \'"
                search_str += vehicle_id
                search_str +=  "\'"
                print(search_str)
                curs.execute(search_str)
                result = curs.fetchall()
                
                if (len(result) == 0):
                    addvehicle(curs,connection,vehicle_id)
                    break
                else:            
                    print("vehicle already exists,")
            is_primary_owner = input("is he/she primary owner of this vehicle? (y) or (n) ").lower()
            while(is_primary_owner != 'y' or is_primary_owner != 'n'):
                if (is_primary_owner == 'y'):
                    break
                if (is_primary_owner == 'n'):
                    break                
                is_primary_owner = input("is he/she primary owner of this vehicle? (y) or (n) ").lower()
                
            
            query = """insert into owner values(
            :owner_id,
            :vehicle_id,
            :is_primary_owner)"""
            try:
                curs.execute(query,{'owner_id':owner_id,
                                    'vehicle_id':vehicle_id,
                                    'is_primary_owner':is_primary_owner}
                             )
                print("New ownership successfully added.")
                connection.commit()
                return True
            except cx_Oracle.IntegrityError as ie:
                print("An integrity error was thrown.")
                print("The Serial you attemped to enter already exists in the database.")
                return False
            except Exception as e:
                errs, = e.args
                print("Oops, an exception was thrown.")
                print("Error code:" + str(errs.code))
                print("Error message:" + errs.message)
                return False            
            connection.commit()
            own = input("enter another owner/vehicle? (y) or (n) or (e) to exit> ").lower()
            if (own == 'e'):
                ownbool = True
            if (own == 'n'):
                ownbool = True


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
'''

def main():
    connection, curs = connect()
    if connection == 0:
        print("Error connecting to database")
        return
    
    print("Main Menu")
    print("Choose the number of function")
    print("1. New Vehicle Registration (n)")
    print("2. Auto Transaction (a)")
    print("3. Driver Licence Registration (d)")
    print("4. Violation Record (v)")
    print("5. Search Engine (s)")
    print("type quit(q) to quit, cls(c) to clear screen")
    print("type menu(m) to display menu")

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
            autoTransaction(curs, connection)
        elif inp == '3' or inp == 'd':
            inp = '3'
            while inp == '3':
                driverLicenceRegistration(curs, connection)
                inp = input("Do you want to register another licence? (y/n) > ").lower()
                while True:
                    if inp == 'y' or inp == 'yes':
                        inp = '3'
                        break
                    elif inp == 'n' or inp == 'no' or inp == 'quit':
                        inp = 'zzzzz'
                        break
                    else:
                        inp = input("Please answer yes(y) or no(n) > ").lower()
        elif inp == '4' or inp == 'v':
            violationRecord(curs, connection)
        elif inp == '5' or inp == 's':
            searchEngine(curs, connection)
        elif inp == 'cls' or inp == 'c':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Main Menu")
            print("1. New Vehicle Registration (n)")
            print("2. Auto Transaction (a)")
            print("3. Driver Licence Registration (d)")
            print("4. Violation Record (v)")
            print("5. Search Engine (s)")
            print("type quit(q) to quit, cls(c) to clear screen")
            print("type menu(m) to display menu")
        elif inp == 'menu' or inp == 'm':
            print("Main Menu")
            print("1. New Vehicle Registration (n)")
            print("2. Auto Transaction (a)")
            print("3. Driver Licence Registration (d)")
            print("4. Violation Record (v)")
            print("5. Search Engine (s)")
            print("type quit to quit(q), cls(c) to clear screen")
            print("type menu(m) to display menu")
        else:
            print("Invalid")
        print(inp)

    cursor.close()
    connection.close()
    return

if __name__ == "__main__":
    main()
