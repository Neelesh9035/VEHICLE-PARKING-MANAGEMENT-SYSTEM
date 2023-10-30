import mysql.connector as sql

con = sql.connect(host="localhost", user="root", passwd="",
                  database="anish")  # to establish connection with mysql connector
cur = con.cursor()

class Search :
    def searchvehtype(self):
        print("")
        print("Searching your vehicle by your vehicle type")
        vtype = input("Enter your vehicle type(car/bike/bus/truck/scooty) : ")
        query = "select * from vehicleparking where vehtype='{}';".format(vtype)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("There is no registration having vehicle type", vtype)
        else:
            print("Details of the people who parked ", vtype)
            cust = 1
            for i in res:
                print("Serial Number", cust)
                print("Center Name : ", i[0])
                print("Name : ", i[1])
                print("Vehicle Number : ", i[2])
                print("Parking lot : ", i[4])
                cust += 1


    def searchcenter(self):
        print("")
        print("Seacrching your vehicle by center")
        print("""Center Names are :
NitteMeenakshi
BagalurCross
Hebbal
Yelahanka
RTNagar""")
        cen = input("Enter the center name where you have parked your vehicle : ")
        query = "select * from vehicleparking where center='{}' ;".format(cen)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("There is no registration in center", cen)
        else:
            print("Details of the people who parked their vehicle in", cen, "center")
            cust = 0
            for i in res:
                print("Serial Number", cust + 1)
                print("Name : ", i[1])
                print("Vehcile Number : ", i[2])
                print("Vehicle Type : ", i[3])
                print("Parking lot : ", i[4])
                cust += 1


    def searchvehno(self):
        print("")
        print("Searching your vehicle by vehicle number")
        vehno = input("Enter your vehicle number : ")
        veh = vehno.lower()
        query = "select * from vehicleparking where vehno='{}';".format(veh)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("There is no registration having vehicle number", vehno)
        for i in res:
            print("Center Name : ", i[0])
            print("Name : ", i[1])
            print("Vehicle number : ", i[2])
            print("Vehicle type : ", i[3])
            print("Parking lot : ", i[4])