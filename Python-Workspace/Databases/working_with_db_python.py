import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="Skippy101!"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE my_database")