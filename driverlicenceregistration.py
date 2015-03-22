'''
Register one person (sin) with a driver licence.
- If that person does not exist in database, user has an option to add that
    person to the database
- If that person already have a driver licence, raise an error message and
    return

Not tested yet
Make sure having addperson.py along with this file when testing.
'''

import random

def driverlicenceregistration(curs, connection):
    # SIN number of the driver
    sin_num = input("input SIN number: ")

    # check if the person exist in the database
    curs.execute("select sin from people")
    rows = curs.fetchall()
    exist = False
    for row in rows:
        if sin_num == row:
            exist = True
            break

    # if the person does not exist, ask the user to 
    #   add that person to database
    if not exist:
        print("Invalid SIN")
        while True:
            inp = input("Do you want to add the person to database?(y/n) ").lower()
            if inp == 'y' or inp == 'yes':
                addperson(curs, connection, sin_num)
                break
            elif inp == 'n' or inp == 'no':
                print("Invalid sin")
                return
            else:
                continue

    # if that person already have a drive_licence, then exit the program 
    curs.execute("select sin from drive_licence")
    rows = curs.fetchall()
    for row in rows:
        if sin_num == row:
            print("The person already have a drive_licence")
            return

    # input class
    drive_class = input("Enter class >")

    # issuing_date = current time, expiring_date = issuing_date + 5 years
    issuing_date = datetime.datetime.now().date()
    expiring_date = datetime.date(issuing_date.year+5, issuing_date.month, issuing_date.day)

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
        for row in rows:
            if licence_no == row:
                exist = True
                break
        exist = False



    # load image into memory from local file
    while True:
        image_name = input("input image name: ")
        try:
            f_image = open(image_name, 'rb')
            image = f_image.read()
            break
        except:
            print("Unable to load image file")
            continue
    f_image.close()

    # prepare memory for operation parameters
    curs.setinputsizes(image = cx_Oravle.BLOB)

    curs.execute("insert into drive_licence "
                 "values(:licence_no, :sin, :class, :photo, :issuing_date, :expiring_date)", {'licence_no':licence_no, 'sin':sin_num, 'class':drive_class, 'photo': image, 'issuing_date':issuing_date.strftime('%d-%b-%Y'), 'expiring_date':expiring_date.strftime('%d-%b-%Y')})

    connection.commit()

    print("Drive licence registered for", sin_num, "with licence_no", licence_no)
    return
