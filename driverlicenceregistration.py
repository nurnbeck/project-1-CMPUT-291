'''
Register one person (sin) with a driver licence.
- If that person does not exist in database, user has an option to add that
    person to the database
- If that person already have a driver licence, raise an error message and
    return

'''

import random
import cx_Oracle
import datetime
from addperson import *

def driverLicenceRegistration(curs, connection):
    # SIN number of the driver
    sin_num = input("input SIN number > ")
    while len(sin_num) > 15 or len(sin_num) == 0:
        sin_num = input("invalid input, please provide driver's sin >")

    # check if the person exist in the database
    curs.execute("SELECT sin FROM PEOPLE")
    rows = curs.fetchmany()
    exist = False
    print("ROWS", rows)
    for row in rows:
        rsin = row[0].strip()
        print("Rsin", rsin)
        if sin_num == rsin:
            exist = True
            break
    print("Exist", exist)
    # if the person does not exist, ask the user to 
    #   add that person to database
    if not exist:
        print("Invalid SIN")
        while True:
            inp = input("Do you want to add the person to database?(y/n) ").lower()
            if inp == 'y' or inp == 'yes':
                check = addperson(curs, connection, sin_num)
                if check:
                    break
                else:
                    print("Error adding person to the database")
                    continue
            elif inp == 'n' or inp == 'no':
                print("Invalid sin")
                return
            else:
                continue

    # if that person already have a drive_licence, then exit the program 
    curs.execute("select sin from drive_licence")
    rows = curs.fetchall()
    for row in rows:
        if sin_num == row[0].strip():
            print("The person already have a drive_licence")
            return

    # input class
    drive_class = input("Enter class >")

    # input issuing date and expiring date
    issuing_date = input("Input issuing date (mm-dd-yyyy) >")
    expiring_date = input("Input expiring date (mm-dd-yyyy) >")

    # generates random licence number
    exist = True

    while exist:
        licence_no = ''
        for i in range(3):
            licence_no += chr(random.randint(ord('a'), ord('z')))
        for i in range(12):
            licence_no += str(random.randint(0,9))
        curs.execute("select licence_no from drive_licence")
        rows = curs.fetchall()
        print("Generated", licence_no)
        print("Licence lst", rows)
        if len(rows) == 0:
            print("NO LICENCE")
            break
        for row in rows:
            print(row)
            if licence_no == row[0]:
                exist = True
                break
            else:
                exist = False
    
    print(licence_no)

    # load image into memory from local file
    while True:
        image_name = input("input image name, type exit to quit > ")
        if image_name == 'exit':
            return
        try:
            f_image = open(image_name, 'rb')
            image = f_image.read()
            break
        except:
            print("Unable to load image file")
            continue

    # prepare memory for operation parameters
    curs.setinputsizes(photo = cx_Oracle.BLOB)

    query = """insert into drive_licence(licence_no, sin, class, photo, issuing_date, expiring_date) values(
    :licence_no,
    :sin,
    :class,
    :photo,
    to_date(:issuing_date, 'MM-DD-YYYY'),
    to_date(:expiring_date, 'MM-DD-YYYY'))"""

    try:
        curs.execute(query, {'licence_no':licence_no, 'sin':sin_num, 'class':drive_class,'photo':image, 'issuing_date':issuing_date, 'expiring_date':expiring_date})

        connection.commit()

        print("Drive licence registered for", sin_num, "with licence_no", licence_no)

    except:
        print("Unknown error occured, adding drive licence failed")

    f_image.close()

    return
