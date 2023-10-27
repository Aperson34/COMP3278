import mysql.connector #MySQL API Library


mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="databasename") #change the password & database


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM admin") #input instructions

myresult = mycursor.fetchall() #get results
for x in myresult:
  print(x)  #a tuple of each row's element
