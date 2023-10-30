import mysql.connector as sql
from Registration import Register
from Displaying import Display
from Searching import Search
from Modification import Modify
from Deletion import Delete
con = sql.connect(host="localhost", user="root", passwd="",
                  database="anish")  # to establish connection with mysql connector
cur = con.cursor()

Reg = Register()
Dpl = Display()
Srch = Search()
Mdfy = Modify()
Del = Delete()

# "if not exists " is the command used to create tables if they do no exist
# so that we do not need to drop the table everytime and create newone
query_1 = '''create table if not exists vehicleparking
(                
center varchar(35),
name varchar(30),
vehno varchar(20),
vehtype varchar(15),
pklot int
);
'''
cur.execute(query_1)  # to execute queries
con.commit()

query_2 = '''create table if not exists centers(
centername varchar(25),
rempklot int
);'''
cur.execute(query_2)
con.commit()

# to check if the values are already there in the centers table or not
querysel = "select * from centers;"
cur.execute(querysel)
totcenters = cur.fetchall()
l=len(totcenters)
if l==0 :
    query_3 = '''insert into centers values(
"NitteMeenakshi",50);'''
    cur.execute(query_3)
    con.commit()

    query_4 = '''insert into centers values(
"BagalurCross",50);'''
    cur.execute(query_4)
    con.commit()

    query_5 = '''insert into centers values(
"Hebbal",50);'''
    cur.execute(query_5)
    con.commit()

    query_6 = '''insert into centers values(
"Yelahanka",50);'''
    cur.execute(query_6)
    con.commit()

    query_7 = '''insert into centers values(
"RTNagar",50);'''
    cur.execute(query_7)
    con.commit()

dash = "=" * 131
square = "-" * 131
title="VEHICLE PARKING SYSTEM"
wel="WELCOME"
x=title.center(120)
y=wel.center(120)
print(dash)
print(x)
print(dash)
print(y)
print(dash)
print(
"""

                                                     _..-------++._
                                                _.-'/ |      _||  \"--._
                                        __.--'`._/_\j_____/_||___\    `----.
                                   _.--'_____    |          \     _____    /
                                 _j    /,---.\   |        =o |   /,---.\   |_
                                [__]==// .-. \\==`===========/==// .-. \\=[__]
                                  `-._|\ `-' /|___\_________/___|\ `-' /|_.'
                                        `---'                     `---'

""")
while True:
    print(""" 1 : REGISTER
2 : VIEW REGISTRATIONS DONE TILL NOW
3 : SEARCH YOUR VEHICLE
4 : MODIFY YOUR DETAILS
5 : UNREGISTER
6 : EXIT""")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        print(dash)
        Reg.register()
        print(dash)

    elif choice == 2:
        print(dash)
        Dpl.displayall()
        print(dash)

    elif choice == 3:
        print(dash)
        print("""1 : SEARCH YOUR VEHICLE BY VEHICLE TYPE
2 : SEARCH YOUR VEHICLE BY CENTER
3 : SEARCH YOUR VEHICLE BY VEHICLE'S NUMBER""")
        ch = int(input("Enter your choice : "))
        if ch == 1:
            print(square)
            Srch.searchvehtype()
            print(square)
        elif ch == 2:
            Srch.searchcenter()
            print(square)

        elif ch == 3:
            Srch.searchvehno()
            print(square)

        else:
            print("Invalid Entry")

    elif choice == 4:
        print(dash)
        Mdfy.modifydet()
        print(dash)

    elif choice == 5:
        Del.unregister()
        print(dash)

    elif choice == 6:
        print("Thank you")
        print(dash)
        break

    else:
        print("Invalid entry")

import matplotlib.pyplot as plt


def countallreg():
    query = "select * from vehicleparking;"
    cur.execute(query)
    res = cur.fetchall()
    if len(res) == 0:
        print("No registrations done till now")
    else:
        print("Here is graphical representation of the total registrations done till now in each center")

        query_1 = "select * from  vehicleparking where center='NitteMeenakshi';"
        cur.execute(query_1)
        res1 = cur.fetchall()
        l1 = len(res1)

        query_2 = "select * from  vehicleparking where center='BagalurCross';"
        cur.execute(query_2)
        res2 = cur.fetchall()
        l2 = len(res2)

        query_3 = "select * from  vehicleparking where center='Hebbal';"
        cur.execute(query_3)
        res3 = cur.fetchall()
        l3 = len(res3)

        query_4 = "select * from  vehicleparking where center='Yelahanka';"
        cur.execute(query_4)
        res4 = cur.fetchall()
        l4 = len(res4)

        query_5 = "select * from  vehicleparking where center='RTNagar';"
        cur.execute(query_5)
        res5 = cur.fetchall()
        l5 = len(res5)

        expl = [0, 0, 0, 0, 0]
        if l1 > l2 and l1 > l3 and l1 > l4 and l1 > l5:
            expl[0] = 0.3
        elif l2 > l1 and l2 > l3 and l2 > l4 and l2 > l5:
            expl[1] = 0.3
        elif l3 > l1 and l3 > l2 and l3 > l4 and l3 > l5:
            expl[2] = 0.3
        elif l4 > l1 and l4 > l2 and l4 > l3 and l4 > l5:
            expl[3] = 0.3
        elif l5 > l1 and l5 > l2 and l5 > l3 and l5 > l4:
            expl[4] = 0.3
        else:
            expl = [0, 0, 0, 0, 0]

        totnov = [l1, l2, l3, l4, l5]
        names = ["NitteMeenakshi", "BagalurCross", "Hebbal", "Yelahanka", "RTNagar"]
        colr = ["silver", "cyan", "gold", "yellow", "pink"]
        plt.pie(totnov, labels=names, colors=colr, autopct="%2.2f%%", explode=expl)
        plt.title("Vehicles Registered Percentage")
        plt.show()
        plt.close()


countallreg()
