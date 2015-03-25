import random
from addperson import addperson
def autoTransaction(curs,connection):
       another_round = True
       foo = True
       quit = False
       keepon = True
       while another_round:
              transaction_id = random.randint(0,999999999)
              valid = False
              while not valid:
                     search_str = ("SELECT * FROM auto_sale a WHERE a.transaction_id = "+ str(transaction_id))
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = True
                     else: 
                            valid = False
              
              
              valid = False
              while not valid:
                     seller_id = str(input("Enter the SIN of the seller: "))
                     search_str = "SELECT name FROM people p WHERE p.sin = "
                     search_str += "\'"
                     search_str += seller_id
                     search_str += "\'"                     
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = False
                            print("Do you want you add a new person? y/n")
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
                     
              
              valid = False
              while not valid and foo and keepon:
                     buyer_id = str(input("Enter the SIN of the buyer: "))
                     search_str = "SELECT name FROM people p WHERE p.sin ="
                     search_str += "\'"
                     search_str += buyer_id
                     search_str += "\'"
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = False
                            print("Do you want you add a new person? y/n")
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

                            
                           
				   
			
              
              
              valid = False
              while not valid and foo and keepon:
                     vehicle_id = str(input("Enter the vehicle id: "))
                     search_str = "SELECT * FROM vehicle v WHERE v.serial_no = "
                     search_str += "\'"
                     search_str += vehicle_id
                     search_str += "\'"
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = False
                            print("The vehicle does not exist in the data base. Please enter valid vehicle id\n")
                            answer = 'a'
                            while not (answer =='y' or answer =='n'):
                                   answer = str(input('Do you want to keep on? y/n'))
                            if answer == 'y':
                                   keepon = True
                            else :
                                   keepon = False


                     else: 
                            search_str = "SELECT * FROM vehicle v WHERE v.serial_no = "
                            search_str += "\'"
                            search_str += vehicle_id
                            search_str += "\'"
                            curs.execute(search_str)
                            result = curs.fetchall()
                            if len(result) == 0:
                                   valid = False
                                   print("This vehicle is not registered in the system\n")
                                   
                            else:
                                   astring = "SELECT o.vehicle_id FROM owner o WHERE o.owner_id = "
                                   astring += "\'"
                                   astring += seller_id
                                   astring += "\'"
                                   curs.execute (astring)
                                   result = curs.fetchall()
                                   own = False
                                   for row in result:
                                          if str(row) == str("(\'"+vehicle_id+"\',)"):
                                                 
                                                 own= True
                                                 
                                   if own == True:
                                          valid = True
                                   else:
                                          print("Seller is not the owner of this vehicle! Please enter another vehicle.")
       
              # check format?
              if foo and keepon:
                     date = input("Enter the date when the transaction happened: ")
              
              
              # need to check if there's exactly two digits after the point?
              
              valid = False
              while not valid and foo and keepon:
                     price = float(input("Enter the price: "))
                     if price > 10000000:
                            valid = False
                            print("Please enter a valid price: ")
                            answer = 'a'
                            while not (answer =='y' or answer =='n'):
                                   answer = str(input('Do you want to keep on? y/n'))
                            if answer == 'y':
                                   keepon = True
                            else :
                                   keepon = False                            

                     else:
                            valid = True
              if foo and keepon:              
                     exe_str = "DELETE FROM owner o WHERE o.owner_id = "
                     exe_str += "\'"
                     exe_str += str(seller_id)
                     exe_str += "\'"
                     curs.execute(exe_str)
                     
                     curs.execute("INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price) VALUES (" + str(transaction_id)+  ",\'"+ str(seller_id)+ "\'"+    ",\'"+str(buyer_id)+"\'"+     ",\'"+str(vehicle_id)+"\'"  +",TO_DATE("+"\'"+str(date)+"\'"+ ","+"'DD-Mon-YYYY')"+    ","+str(price)+")")
                     print("Data inserted succesfully.\n")
              
              valid = False
              while not valid:
                     answer = input("Do you want to enter another auto transaction record? y/n")
                     if answer == 'y' or 'n':
                            valid = True
                            if answer == 'y':
                                   another_round = True
                                   foo = True
                                   keepon = True
                                   print("\nEnter another auto transaction record - \n")
                            else:
                                   another_round = False
                                   print("\nThe end of this transaction record\n")
                     else:
                            valid = False              
