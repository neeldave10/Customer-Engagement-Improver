import mysql.connector

class Database:
    cnx = mysql.connector.connect(user='root', password='neel123', host='localhost', database='sentiments')
    mycursor = cnx.cursor()

    def getSentiment(self,s):
        sql="SELECT sentiment FROM customer where customerid=%s"
        arg=(s,)
        Database.mycursor.execute(sql,arg)
        myresult = Database.mycursor.fetchall()
        return myresult

    def changingSentiment(self,str,id):
        sql="Update customer set sentiment=%s where customerid=%s"
        arg=(str,id)
        Database.mycursor.execute(sql, arg)
        Database.cnx.commit()
        return "Updated successfully"






