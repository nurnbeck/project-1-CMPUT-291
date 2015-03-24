import random
from addperson import *

def violationRecord(curs,connection):
    another_round = True
    foo = True
    quit = False    
    while another_round:
        answer = 'a'
        while not (answer == '1' or answer == '2'):
            answer = str(input("Record for 1. primary owner\n2.a given driver"))
        if answer == 'y':
            ownerfault = True
        else:
            ownerfault = False
            
        
                         
        valid = False
        while not valid and not ownerfault:
            seller_id = str(input("Enter the SIN of the violator: "))
            search_str = "SELECT name FROM people p WHERE p.sin = "
            search_str += "\'"
            search_str += seller_id
            search_str += "\'"                     
            curs.execute(search_str)
            result = curs.fetchall()
            if len(result) == 0:
                valid = False
                print("The person does not exist. Do you want you add a new person? y/n")
                answer = str(input())
                
                while not (answer =='y' or answer == 'n'):
                    answer = str(input("Please enter y or n"))
                if answer =='y':
                    foo = addperson(curs, connection)
                    quit = False
                        
                    while foo == False:
                            
                        answer = 'a'
                        while not (answer =='y' or answer == 'n'):
                            answer =  str(input("Do you want to keep adding a new person? y/n\n"))
                            if answer =='y':
                                foo = addperson(curs, connection)
                            else:
                                quit = True
                                break
                        if quit:
                            break
                elif quit:
                    break
                                
                else:
                    foo = False
                    break
                            
                            
            else: 
                valid = True
                            
            if quit:
                break           
        
     
        # get vehicle id
        valid = False
        while not valid and foo:
            vehicle_id = str(input("Enter the serial number of the vehicle involved: "))
            search_str = "SELECT * FROM vehicle v WHERE v.serial_no = "
            search_str += "\'"
            search_str += vehicle_id
            search_str += "\'"
            curs.execute(search_str)
            result = curs.fetchall()
            if len(result) == 0:
                valid = False
                print("Please enter valid vehicle id\n")
            else: 
                valid = True     
        #if ownerfault == True:
         #   seller_id
        
        
        # get officer number
        valid = False
        while not valid and foo:
            office_no = str(input("Enter the SIN of the officer: "))
            search_str = "SELECT name FROM people WHERE p.sin = "
            search_str += "\'"
            search_str += office_no
            search_str += "\'"
            curs.execute(search_str)
            result = curs.fetchall()
            if len(result) == 0:
                valid = False
                print("Please enter SIN\n")
            else: 
                valid = True            


        valid = False
        while not valid and foo:
            vtype = input("Enter valid vehicle type: ")
            search_str = "SELECT * FROM ticket_type v WHERE v.vtype = "
            search_str += "\'"
            search_str += vtype
            search_str += "\'"
            curs.execute(search_str)
            result = curs.fetchall()
            if len(result) == 0:
                valid = False
                print("Please enter vehicle type\n")
            else: 
                valid = True            
        if foo:
            date = input("Enter the date when the accident happened: ")
            # ################################### check if date entered is valid ####################
        
            place = input("Enter the place where the accident happened: ")        
            descriptions = input("Enter description of the accident: ")
            
            curs.execute("INSERT INTO ticket(ticket_no, name, violator_no, vehicle_id, office_no, vtype, vdate, place, descriptions) VALUES (" + ticket_no  +  ", \'" + violator_no + "\'" + ", \'" + vehicle_id+ "\'"+ ", \'" + office_no + "\'"    +  ", \'" + vtype + "\'" +     ", \'" +date+ "\'"+     ", \'"+place+"\'"+    ", \'"+descriptions+ " \')") 
        
        valid = False
        while not valid:
            answer = input("Do you want to enter another violation record? y/n").lower()
            if answer == 'y' or 'n':
                valid = True
                if answer == 'y':
                    another_round = True
                    print("\nEnter another violation record - \n")
                else:
                    another_round = False
                    print("\nThe end of this record\n")
            else:
                valid = False
