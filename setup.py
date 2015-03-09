import cx_Oracle

'''
- This is to drop all pervious tables and create new tables
- Call setup(curs, connection) in main function
- setup(curs, connection) returns nothing
- Do not call dropTable() and createTable() in main
    unless you really want to do so
'''

def dropTable(curs):
    droplst = []
    droplst.append("drop table owner")
    droplst.append("drop table auto_sale")
    droplst.append("drop table restriction")
    droplst.append("drop table driving_condition")
    droplst.append("drop table ticket")
    droplst.append("drop table ticket_type")
    droplst.append("drop table vehicle")
    droplst.append("drop table vehicle_type")
    droplst.append("drop table drive_licence")
    droplst.append("drop table people")
    for i in range(len(droplst)):
        try:
            curs.execute(droplst[i])
        except:
            pass
    return


def createTable(curs):
    createPeople = ("create table people "
                    """(sin CHAR(15), name VARCHAR(40), height number(5, 2),
                    weight number(5, 2), eyecolor VARCHAR(10), haircolor VARCHAR(10),
                    addr VARCHAR2(50), gender CHAR, birthday DATE)""")
    createdrive_licence = ("create table drive_licence "
                        """(licence_no CHAR(15), sin CHAR(15), class VARCHAR(10),
                        photo BLOB, issuing_date DATE, expiring_date DATE)""")
    createdriving_condition = ("create table driving_condition "
                            """(c_id INTEGER, description VARCHAR(1024))""")
    createrestriction = ("create table restriction "
                         """(licence_no CHAR(15), r_id INTEGER)""")
    createvehicle_type = ("create table vehicle_type "
                          """(type_id INTEGER, type CHAR(10))""")
    createvehicle = ("create table vehicle "
                     """(serial_no CHAR(15), maker VARCHAR(20), model VARCHAR(20),
                     year number(4, 0), color VARCHAR(10), type_id INTEGER)""")
    createowner = ("create table owner "
                   """(owner_id CHAR(15), vehicle_id CHAR(15),
                   is_primary_owner CHAR(1))""")
    createauto_sale = ("create table auto_sale "
                       """(transaction_id int, seller_id CHAR(15), buyer_id CHAR(15),
                       vehicle_id CHAR(15), s_date date, price numeric(9, 2))""")
    createticket_type = ("create table ticket_type "
                         """(vtype CHAR(10), fine number(5, 2))""")
    createticket = ("create table ticket "
                    """(ticket_no int, violator_no CHAR(15), vehicle_id CHAR(15),
                    office_no CHAR(15), vtype CHAR(10), vdate date, place VARCHAR(20),
                    descriptions VARCHAR(1024))""")
    
    curs.execute(createPeople)
    curs.execute(createdrive_licence)
    curs.execute(createdriving_condition)
    curs.execute(createrestriction)
    curs.execute(createvehicle_type)
    curs.execute(createvehicle)
    curs.execute(createowner)
    curs.execute(createauto_sale)
    curs.execute(createticket_type)
    curs.execute(createticket)

    return


def setup(curs, connection):
    dropTable(curs)
    createTable(curs)
    connection.commit()
    return
