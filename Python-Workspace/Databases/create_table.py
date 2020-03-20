import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="Skippy101!",
  database="my_database"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")