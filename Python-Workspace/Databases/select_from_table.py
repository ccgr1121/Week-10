import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="my_database"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for customer in myresult:
  print(customer)