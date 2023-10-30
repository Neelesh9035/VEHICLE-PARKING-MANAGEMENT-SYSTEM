import mysql.connector as sql
con = sql.connect(host="localhost", user="root", passwd="",
                  database="anish")  # to establish connection with mysql connector
cur = con.cursor()
class Register :
    def register(self):  # to insert the details of the customers into the needed tables

        print("Registering your vehicle")
        while True:
            pklot = 0
            print("Centers are : ")
            print("""
1 : NitteMeenakshi
2 : BagalurCross
3 : Hebbal 
4 : Yelahanka
5 : RTNagar
""")
            center = ""
            ch = int(input("Enter your choice : "))
            if ch == 1:
                center = "NitteMeenakshi"
            elif ch == 2:
                center = "BagalurCross"
            elif ch == 3:
                center = "Hebbal"
            elif ch == 4:
                center = "Yelahanka"
            elif ch == 5:
                center = "RTNagar"
            else:
                print("Invalid entry")
                print("Try again")
                self.register()
                break
            name = input("Enter your name : ")
            vehno = input("Enter your vehicle number : ")
            veh = vehno.lower()
            vehtype = input("Enter vehicle type(car/bike/scooty/truck/bus): ")
            vehtypelist=["car","bike","scooty","truck","bus"]
            if vehtype not in vehtypelist:
                print(""".Sorry.
INVALID ENTRY OR THIS TYPE OF VEHICLE IS NOT ALLOWED
TRY AGAIN NEXT TIME""")
                break
            query_1 = "select count(*) from vehicleparking where center='{}';".format(center)
            cur.execute(query_1)
            res = cur.fetchall()
            l = len(res)
            if (l == 50):
                print("Sorry no space at this center")
                CH = input("Do you want to try in another center?(Y/N) : ")
                if CH == "N":
                    return None
                elif CH == "Y":
                    self.register()
            else:
                query_2 = "select pklot from vehicleparking where center='{}' order by pklot asc;".format(center)
                cur.execute(query_2)
                res2 = cur.fetchall()
                le = len(res2)

                if le == 0:
                    pklot = 1

                else:
                    pklot = -1
                    num = 0;
                    for i in res2:
                        for j in i:
                            num = num + 1
                            if j != num:
                                pklot = num
                                break
                    if (pklot == -1):
                        pklot = num + 1
                    centersquery="update centers set rempklot={} where centername='{}';".format(50-pklot,center)
                    cur.execute(centersquery)
                    con.commit()

            query_3 = "insert into vehicleparking values('{}','{}','{}','{}',{});".format(center, name, veh, vehtype,
                                                                                      pklot);
            cur.execute(query_3)
            con.commit()

            """
            query_4 = "insert into {}center values({},'{}','{}','{}');".format(center, pklot, name, veh, vehtype);
            cur.execute(query_4)
            con.commit()
            """

            print("Vehicle registered")
            print(" Your Parking lot is ", pklot)
            print("Thank You")
            c = input("EXIT?(Y/N) :").lower()
            if c == "y":
                break
