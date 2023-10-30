import mysql.connector as sql
con = sql.connect(host="localhost", user="root", passwd="",
                  database="anish")  # to establish connection with mysql connector
cur = con.cursor()
class Delete :
    def unregister(self):  # to delete records from the tables
        center = input("Enter your center name : ")
        vehno = input("Enter your vehicle number : ")
        veh = vehno.lower()
        basequery = "select * from vehicleparking where center='{}' and vehno='{}';".format(center, veh)
        cur.execute(basequery)
        res = cur.fetchall()
        l = len(res)
        if l == 0:
            print("Sorry no registration is there having center name as", center, "and vehicle number as", veh)
        else:
            query_1 = "delete from vehicleparking where center='{}' and vehno='{}';".format(center, veh)
            cur.execute(query_1)
            centersquery="update centers set rempklot=rempklot+1 where centername='{}';".format(center)
            cur.execute(centersquery)
            con.commit()
            print("You have succesfully unregistered.")
            print("Thank you.")