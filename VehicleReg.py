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
