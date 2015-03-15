def searchEngine(curs, connection):
       print("Search Engine")
       stop = False
       while not stop:
              
              
              validity = False
              while not (validity == 1 or validity == 2 or validity == 3):
                     print("\nPlease enter the correct option")
                     option = input("Enter the option - 1. Driver's Info \n2. Violation Records \n3. Vehilce History \n")
                     validity = checkInput(option)
                     
                     
              if validity == 1:
                     search_by = False
                     while not (search_by == 1 or search_by == 2):
                            print("\nDriver's Info - Please enter the correct option")
                            search_no = input("Search by  - 1. Name \n2. Liscence No \n")
                            search_by = checkInput(search_no)
                            
                     if search_by == 1:
                            nameorsin = str(input("Driver's Info - Enter Name: "))
                            
                            search_str = ("SELECT name, licence_no, addr, birthday, class, description, expiring_data FROM people p, drive_licence d, driving_condition dc, restriction r WHERE p.sin = d.sin AND d.licence_no = r.licence_no AND r.r_id = dc.c_id AND p.name = ",nameorsin,";")
                            curs.execute(search_str)
                            result = curs.fetchall()
                            print("Driver's Info - people with Name: ",nameorsin)
                            if len(result) == 0:
                                   print("No matching result")        
                            else:
                                   for i in result:
                                          print(i)
                                   
                     if search_by == 2:
                            nameorsin = input("Driver's Info - Enter SIN: ")
       
                            search_str = ("SELECT name, licence_no, addr, birthday, class, description, expiring_data FROM people p, drive_licence d, driving_condition dc, restriction r WHERE p.sin = d.sin AND d.licence_no = r.licence_no AND r.r_id = dc.c_id AND p.sin = ",int(nameorsin),";")
                            curs.execute(search_str)    
                            result = curs.fetchall()
                            print("Driver's Info - people with SIN: ",nameorsin)
                            if len(result) == 0:
                                   print("No matching result")  
                            else:
                                   for i in result:
                                          print(i)                                   
                            
              if validity == 2:
                     search_by = False
                     while not (search_by == 1 or search_by == 2):
                            print("\nViolation Records - Please enter the correct option")
                            search_no = input("Search by  - 1. Liscence No. \n2. SIN \n")
                            search_by = checkInput(search_no)
                            
                     if search_by == 1:
                            noorsin = input("Violation Records - Please enter correct Liscence Number: ")
              
                            search_str = ("SELECT name, licence_no, ticket_no, violator_no, vehicle_id, office_no, vtype, vdate, place, fine, descriptions FROM people p, ticket t, ticket_type tt, drive_licence d WHERE p.sin = t.violator_no AND t.vtype == tt.vtype AND p.sin = d.sin AND d.licence_no = ",int(noorsin),";")
                            curs.execute(search_str)    
                            result = curs.fetchall()
                            print("Violation Records - people with Liscence Number: ",noorsin)
                            if len(result) == 0:
                                   print("No matching result")  
                            else:
                                   for i in result:
                                          print(i)
                     
                     if search_by == 2:
                            noorsin = input("Violation Records - Please enter correct SIN: ")
 
                            search_str = ("SELECT name, ticket_no, violator_no, vehicle_id, office_no, vtype, vdate, place, fine, descriptions FROM people p, ticket t, ticket_type tt WHERE p.sin = t.violator_no AND t.vtype == tt.vtype AND p.sin = ",int(noorsin),";")
                            curs.execute(search_str)    
                            result = curs.fetchall()
                            print("Violation Records - people with SIN: ",noorsin)
                            if len(result) == 0:
                                   print("No matching result")  
                            else:
                                   for i in result:
                                          print(i)                     
                     
                     
              if validity == 3:
                     serialnumber = input("Vehicle History - Please enter correct Serial Number: ")
              
                     search_str = # ###############################################
                     curs.execute(search_str)    
                     result = curs.fetchall()
                     print("Vehicle History - Vehicle with Serial Number: ",serialnumber)
                     if len(result) == 0:
                            print("No matching result")  
                     else:
                            for i in result:
                                   print(i)                     
                     
              
              another_round= str(input("\nDo you want to perform another search? y/n\n")).lower()
              while not ( another_round == 'y' or another_round == 'n'):    
                     print("\nPlease enter valid input")
                     another_round= str(input("Do you want to perform another search? y/n\n")).lower()
          
              if another_round == 'n':
                     stop = True
                     

def checkInput(variable):
       try:
              integer = int(variable)
              return integer
       except:
              return False
       
