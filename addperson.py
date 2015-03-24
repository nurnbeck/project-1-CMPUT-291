'''
Adds one person to the database
- Does not handle people who were born before christ

tested
'''
import datetime
import cx_Oracle

def addperson(curs, connection, sin = 'zzzzzz'):
    # input sin
    if sin == 'zzzzzz':
        sin = input("Input sin number >")
    while len(sin) > 15:
        print("Invalid input")
        sin = input("Input sin number >")

    # input name
    name = input("Input name >")
    while len(name) > 40:
        print("Invalid input")
        name = input("Input name >")

    # input height
    while True:
        height = input("Input height >")
        if '.' not in height:
            height += '.00'
        elif height[-1] == '.':
            height += '00'
        elif height[-2] == '.':
            height += '0'
        elif height[-3] != '.':
            print("Invalid input")
            continue
        if len(height) > 6:
            print("Invalid input")
            continue
        try:
            height = float(height)
        except:
            print("Invalid input")
            continue
        if height == 0:
            print("Invalid input")
            continue
        break

    # input weight
    while True:
        weight = input("Input weight >")
        if '.' not in weight:
            weight += '.00'
        elif weight[-1] == '.':
            weight += '00'
        elif weight[-2] == '.':
            weight += '0'
        elif weight[-3] != '.':
            print("Invalid input")
            continue
        if len(weight) > 6:
            print("Invalid input")
            continue
        try:
            weight = float(weight)
        except:
            print("Invalid input")
            continue
        if weight == 0:
            print("Invalid input")
            continue
        break

    # input eyecolor
    eyecolor = input("Input eyecolor >")
    while len(eyecolor) > 10:
        print("Invalid input")
        eyecolor = input("Input eyecolor >")

    # input haircolor
    haircolor = input("Input haircolor >")
    while len(haircolor) > 10:
        print("Invalid input")
        haircolor = input("Input haircolor >")

    # input address
    addr = input("Input address >")
    while len(addr) > 50:
        print("Invalid input")
        addr = input("Input address >")

    # input gender
    #bugged
    gender = input("Input gender (m/f) >").lower()
    while (gender != 'm' or gender != 'f'):
        if (gender == 'm'):
            break
        if (gender == 'f'):
            break        
        print("Invalid input")
        gender = input("Input gender >").lower()
    # input birthday
    while True:
        #i had to change this because of the way SQL formats
        birthday = input("Input birthday (mm-dd-yyyy) >")
        '''
        yi = birthday.find('/')
    
        if yi <= 0:
            print("Invalid input")
            continue
        year = birthday[:yi]
        birthday = birthday[yi+1:]
        mi = birthday.find('/')
        if mi <= 0:
            print("Invalid input")
            continue
        month = birthday[:mi]
        day = birthday[mi+1:]
        try:
            year = int(year)
            month = int(month)
            day = int(day)
        except:
            print("Invalid input")
            continue
        if year < 0:
            print("Invalid input")
            continue
        if month < 1 or month > 12:
            print("Invalid input")
            continue
        if month in [1,3,5,7,8,10,12]:
            if day < 1 or day > 31:
                print("Invalid input")
                continue
        elif month == 2:
            if (not year%400) or ((not year%4) and year%100):
                if day < 1 or day > 29:
                    print("Invalid input")
                    continue
            else:
                if day < 1 or day > 28:
                    print("Invalid input")
                    continue
        else:
            if day < 1 or day > 30:
                print("Invalid input")
                continue
                
        #birthday = '11-11-1995'
        '''
        break
    #fixed
    query = """insert into people values(
    :sin,
    :name,
    :height,
    :weight,
    :eyecolor,
    :haircolor,
    :addr,
    :gender,
    to_date(:birthday, 'MM-DD-YYYY'))"""
    try:
        curs.execute(query,{'sin':sin,
                            'name':name,
                            'height':height,
                            'weight':weight,
                            'eyecolor':eyecolor,
                            'haircolor':haircolor,
                            'addr':addr,
                            'gender':gender,
                            'birthday':birthday}
                     )
        print("New person successfully added.")
        connection.commit()
        return True
    except cx_Oracle.IntegrityError as ie:
        print("An integrity error was thrown.")
        print("The SIN you attemped to enter already exists in the database.")
        return False
    except Exception as e:
        errs, = e.args
        print("Oops, an exception was thrown.")
        print("Error code:" + str(errs.code))
        print("Error message:" + errs.message)
        return False
    
    
