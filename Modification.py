import mysql.connector as sql
con = sql.connect(host="localhost", user="root", passwd="",
                  database="anish")  # to establish connection with mysql connector
cur = con.cursor()
class Modify :
    def modifydet(self):
        print("You can modify your name , vehicle type , vehicle number ")
        cn = input("Enter your center name : ")
        pl = int(input("Enter your parking lot : "))

        query = "select * from vehicleparking where pklot={}  and center='{}';".format(pl, cn)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("Sorry there is no data having parking lot ", pl, "and center name ", cn)
        else:
            print("Here are your previous details ")
            for i in res:
                print("Previous Center Name : ", i[0])
                print("Previous Name : ", i[1])
                print("Previous Vehicle Number : ", i[2])
                print("Previous Vehicle Type : ", i[3])
            n = input("What do you want to modify(name/vehicle number/vehicle type) ? : ")
            mod = input("Enter the modified data : ")
            con.commit()
            while True :
                if n == "vehicle number":
                    query_modify = "Update vehicleparking set vehno='{}' where pklot={} and center='{}';".format(mod, pl, cn)
                    break
                elif n == "vehicle type":
                    query_modify = "Update vehicleparking set vehtype='{}' where pklot={} and center='{}';".format(mod, pl, cn)
                    break
                elif n == "name":
                    query_modify = "Update vehicleparking set name='{}' where pklot={} and center='{}';".format(mod, pl, cn)
                    break
                else :
                    print("wrong input. try again")
            cur.execute(query_modify)
            """cur.execute(query_tablemodify)"""
            print("Modified your details.")