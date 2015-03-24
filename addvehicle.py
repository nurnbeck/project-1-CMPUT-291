'
import datetime
import cx_Oracle

def addvehicle(curs, connection, serial_no = 'zzzzzz'):
    serial_no = input("input serial_no > ")
    while(len(serial_no) > 15):
        serial_no = input("input too long, input serial_no > ")
        
    maker = input("input maker > ")
    while(len(maker) > 20):
        maker = input("input too long, input maker > ")            
        
    model = input("input model > ")
    while(len(serial_no) > 20):
        model = input("input too long, model > ")   
        
    year = input("input year > ")
    while(len(year) > 4):
        year = input("input after 9999, invalid year > ")                   
    color = input("input color > ")
    while(len(color) > 10):
        color = input("input too long, color > ")                   
    type_id = input("input type_id > ")
    while(len(type_id) > 20):
        type_id = input("input too long, type_id > ")         
    #insertion
    query = """insert into people values(
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
