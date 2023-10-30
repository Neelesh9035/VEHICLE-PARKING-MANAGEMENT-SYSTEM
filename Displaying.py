import mysql.connector as sql

con = sql.connect(host="localhost", user="root", passwd="",
                  database="anish")  # to establish connection with mysql connector
cur = con.cursor()

class Display :
    def displayall(self):  # to display the names of the registered customers
        query = "select * from vehicleparking;"
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            print("No registrations done till now")
        else:
            print("Names are : ")
            for i in res:
                print(i[1])