import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="Skippy101!",
  database="my_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")