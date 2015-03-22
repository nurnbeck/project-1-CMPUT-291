import random

def autoTransaction():
       another_round = True
       while another_round:
              transaction_id = random.randint(0,999999999)
              valid = False
              while not valid:
                     search_str = ("SELECT * FROM auto_sale a WHERE a.transaction_id = ", transaction_id)
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = True
                     else: 
                            valid = False
              
              
              valid = False
              while not valid:
                     seller_id = str(input("Enter the SIN of the seller: "))
                     search_str = "SELECT name FROM people WHERE p.sin = "
                     search_str += "\'"
                     search_str += seller_id
                     search_str += "\'"                     
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = False
                            print("Please enter valid sin\n")
                     else: 
                            valid = True
                     
              
              valid = False
              while not valid:
                     buyer_id = str(input("Enter the SIN of the buyer: "))
                     search_str = "SELECT name FROM people WHERE p.sin ="
                     search_str += "\'"
                     search_str += buyer_id
                     search_str += "\'"
                     curs.execute(search_str)
                     result = curs.fetchall()
                     if len(result) == 0:
                            valid = False
                            print("Please enter valid sin\n")
                     else: 
                            valid = True
              
              
              valid = False
              while not valid:
                     vehicle_id = str(input("Enter the vehicle id: "))
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
                                   valid = True
                     
       
              # check format?
              
              date = input("Enter the date when the accident happened: ")
              
              
              # need to check if there's exactly two digits after the point?
              
              valid = False
              while not valid:
                     price = float(input("Enter the price"))
                     if price > 10000000:
                            valid = False
                            print("Please enter a valid price")
                     else:
                            valid = True
              
              exe_str = "DELETE FROM owner o WHERE o.vehicle_id = "
              exe_str += "\'"
              exe_str += vehicle_id
              exe_str += "\'"
              curs.execute(exe_str)
              
              curs.execute("INSERT INTO auto_sale(transaction_id, seller_id, buyer_id, vehicle_id, s_date, price) VALUES (" + transaction_id+  ",\'"+ seller_id+ "\'"+      ",\'"+buyer_id+"\'"+     ",\'"+vehicle_id+"\'"+      ",\'"+s_date+"\'",      "\'"+price+"\')")
              
              valid = False
              while not valid:
                     answer = input("Do you want to enter another auto transaction record? y/n")
                     if answer == 'y' or 'n':
                            valid = True
                            if answer == 'y':
                                   another_round = True
                                   print("\nEnter another auto transaction record - \n")
                            else:
                                   another_round = False
                                   print("\nThe end of this transaction record\n")
                     else:
                            valid = False              
