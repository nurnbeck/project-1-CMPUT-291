import datetime
import cx_Oracle

def addvehicle(curs, connection, serial_no = 'zzzzzz'):
    if serial_no == 'zzzzzz':
        serial_no = input("input serial_no > ")
        while(len(serial_no) > 15 or len(serial_no) == 0):
            serial_no = input("invalid input, input serial_no > ")
        
    maker = input("input maker > ")
    while(len(maker) > 20 or len(maker) == 0):
        maker = input("invalid input, input maker > ")            
        
    model = input("input model > ")
    while(len(serial_no) > 20 or len(serial_no) == 0):
        model = input("invalid input, model > ")   
    
    # year numeric(4, 0)
    year = input("input year > ")
    #while(len(year) > 4 or len(year) == 0):
    while True:
        if len(year) > 4 or len(year) == 0:
            year = input("input after 9999, invalid year > ")
            coninue
        try:
            year = int(year)
            break
        except:
            year = input("invalid input, year > ")
            continue
    color = input("input color > ")
    while(len(color) > 10 or len(color) == 0):
        color = input("invalid input, color > ")                   
    type_id = input("input type_id > ")
    
    #while(len(type_id) > 20 or len(type_id) == 0):
    # tupe_id integer
    while True:
        try:
            type_id = int(type_id)
            break
        except:
            type_id = input("invalid input, type_id > ")
            continue
    #insertion
    query = """insert into vehicle values(
    :serial_no,
    :maker,
    :model,
    :year,
    :color,
    :type_id)"""
    try:
        curs.execute(query,{'serial_no':serial_no,
                            'maker':maker,
                            'model':model,
                            'year':year,
                            'color':color,
                            'type_id':type_id}
                     )
        print("New vehicle successfully added.")
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
