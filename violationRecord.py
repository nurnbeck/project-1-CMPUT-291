import random

def violationRecord():
    another_round = True
    while another_round:
        
        valid = False
        while not valid:
            ticket_no = random.randint(0,999999999)
            search_str = "SELECT * FROM ticket t WHERE t.ticket_no = ", ticket_no
            curs.execute(search_str)
            result = curs.fetchall()
            if len(result) == 0:
                valid = True
            else: 
                valid = False            
        
       
        # get VIOLATOR_NO
        valid = False
        while not valid:
            violator_no = str(input("Enter the SIN of the violator: "))
            search_str = "SELECT name FROM people WHERE p.sin = "
            search_str += "\'"
            search_str += violator_no
            search_str += "\'"
            curs.execute(search_str)
            result = curs.fetchall()
            if len(result) == 0:
                valid = False
                print("Please enter valid sin\n")
            else: 
                valid = True
     
        # get vehicle id
        valid = False
        while not valid:
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
        
        
        # get officer number
        valid = False
        while not valid:
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
        while not valid:
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
