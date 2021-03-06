def searchEngine(curs, connection):
       print("Search Engine")
       stop = False
       while not stop:
              
              
              validity = False
              while not (validity == 1 or validity == 2 or validity == 3):
                     print("\nPlease enter the correct option")
                     option = input("Enter the option - \n1. Driver's Info \n2. Violation Records \n3. Vehilce History \n>")
                     validity = checkInput(option)
                     
                     
              if validity == 1:
                     search_by = False
                     while not (search_by == 1 or search_by == 2):
                            print("\nDriver's Info - Please enter the correct option")
                            search_no = input("Search by  - \n1. Name \n2. Liscence No \n>")
                            search_by = checkInput(search_no)
                            
                     if search_by == 1:
                            nameorno = str(input("Driver's Info - Enter Name: "))
                                             
                            search_str = ("SELECT name, d.licence_no, addr, birthday, class, description, expiring_date FROM people p, drive_licence d, driving_condition dc, restriction r WHERE d.licence_no (+)=r.licence_no AND r.r_id (+)= dc.c_id AND p.sin = d.sin AND p.name =  ")
                            search_str += "\'"
                            search_str += nameorno
                            search_str += "\'"
                            curs.execute(search_str)
                            result = curs.fetchall()
                            print("Driver's Info - people with Name: ",nameorno)
                            if len(result) == 0:
                                   print("No matching result")        
                            else:
                                   print(len(result), "result(s) found")
                                   for i in result:
                                          print("--------------------------------------------")
                                          print("Name             :", i[0])
                                          print("Licence No       :", i[1])
                                          print("Address          :", i[2])
                                          print("Birthday         :", i[3])
                                          print("Class            :", i[4])
                                          print("Driving Condition:", i[5])
                                          print("Expiring Date    :", i[6])
                            
                     if search_by == 2:
                            nameorno = str(input("Driver's Info - Enter Licence No> "))
       
                            search_str = ("SELECT name, d.licence_no, addr, birthday, class, description, expiring_date FROM people p, drive_licence d, driving_condition dc, restriction r WHERE d.licence_no (+)=r.licence_no AND p.sin = d.sin AND r.r_id (+)= dc.c_id AND d.licence_no = ")
                            search_str += "\'"
                            search_str += str(nameorno)
                            search_str += "\'"
                            curs.execute(search_str)    
                            result = curs.fetchall()
                            print("Driver's Info - people with License No: ",nameorno)
                            if len(result) == 0:
                                   print("No matching result")  
                            else:
                                   print(len(result), "result(s) found")
                                   for i in result:
                                          print("--------------------------------------------")
                                          print("Name             :", i[0])
                                          print("Licence No       :", i[1])
                                          print("Address          :", i[2])
                                          print("Birthday         :", i[3])
                                          print("Class            :", i[4])
                                          print("Driving Condition:", i[5])
                                          print("Expiring Date    :", i[6])
                            
              if validity == 2:
                     search_by = False
                     while not (search_by == 1 or search_by == 2):
                            print("\nViolation Records - Please enter the correct option")
                            search_no = input("Search by  - \n1. Liscence No. \n2. SIN \n>")
                            search_by = checkInput(search_no)
                            
                     if search_by == 1:
                            noorsin = str(input("Violation Records - Please enter correct Liscence Number> "))
              
                            search_str = ("SELECT name, d.licence_no, t.ticket_no, t.violator_no, t.vehicle_id, t.office_no, t.vtype, t.vdate, t.place, tt.fine, descriptions FROM people p, ticket t, ticket_type tt, drive_licence d WHERE p.sin = t.violator_no AND t.vtype = tt.vtype AND p.sin = d.sin AND d.licence_no = ")
                            search_str += "\'"
                            search_str += noorsin
                            search_str += "\'"
                            curs.execute(search_str)    
                            result = curs.fetchall()
                            print("Violation Records - people with Liscence Number: ",noorsin)
                            if len(result) == 0:
                                   print("No matching result")  
                            else:
                                   print(len(result), "result(s) found")
                                   for i in result:
                                          print("--------------------------------------------")
                                          print("Name           :", i[0])
                                          print("Licence No     :", i[1])
                                          print("Ticket No      :", i[2])
                                          print("Violator No    :", i[3])
                                          print("Vehicle ID     :", i[4])
                                          print("Office No      :", i[5])
                                          print("Violation Type :", i[6])
                                          print("Violation Date :", i[7])
                                          print("Violation Place:", i[8])
                                          print("Fine           :", i[9])
                                          print("Description    :", i[10])
                                          
                     
                     if search_by == 2:
                            noorsin = str(input("Violation Records - Please enter correct SIN> "))
 
                            search_str = ("SELECT name, t.ticket_no, t.violator_no, t.vehicle_id, t.office_no, t.vtype, t.vdate, t.place, tt.fine, descriptions FROM people p, ticket t, ticket_type tt WHERE p.sin = t.violator_no AND t.vtype = tt.vtype AND p.sin = ")
                            search_str += "\'"
                            search_str += noorsin
                            search_str += "\'"
                            curs.execute(search_str)    
                            result = curs.fetchall()
                            print("Violation Records - people with SIN: ",noorsin)
                            if len(result) == 0:
                                   print("No matching result")  
                            else:
                                   print(len(result), "result(s) found")
                                   for i in result:
                                          print("--------------------------------------------")
                                          print("Name           :", i[0])
                                          print("Ticket No      :", i[1])
                                          print("Violator No    :", i[2])
                                          print("Vehicle ID     :", i[3])
                                          print("Office No      :", i[4])
                                          print("Violation Type :", i[5])
                                          print("Violation Date :", i[6])
                                          print("Violation Place:", i[7])
                                          print("Fine           :", i[8])
                                          print("Description    :", i[9])
                     
              if validity == 3:
                     serialnumber = str(input("Vehicle History - Please enter correct Serial Number> "))
              
                     search_str = ("SELECT COUNT(transaction_id), AVG(price), COUNT(ticket_no) FROM auto_sale a, ticket t WHERE a.vehicle_id = ")
                     search_str += "\'"
                     search_str += serialnumber
                     search_str += "\'"
                     search_str += " AND t.vehicle_id = "
                     search_str += "\'"
                     search_str += serialnumber
                     search_str += "\'"
                     curs.execute(search_str)    
                     result = curs.fetchall()
                     print("Vehicle History - Vehicle with Serial Number: ",serialnumber)
                     if len(result) == 0:
                            print("No matching result")  
                     else:
                            print(len(result), "result(s) found")
                            for i in result:
                                   print("--------------------------------------------")
                                   print("Transaction Times  :", i[0])
                                   print("Average Price      :", i[1])
                                   print("Number of Violation:", i[2])
                     
              
              another_round= str(input("\nDo you want to perform another search? y/n >")).lower()
              while not ( another_round == 'y' or another_round == 'n'):    
                     print("\nPlease enter valid input")
                     another_round= str(input("Do you want to perform another search? y/n >")).lower()
          
              if another_round == 'n':
                     stop = True
                     

def checkInput(variable):
       try:
              integer = int(variable)
              return integer
       except:
              return False
       
