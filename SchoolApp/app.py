print("Content-Type:text/html")
print()

import mysql.connector, cgi

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="schoolappdb"
)

form = cgi.FieldStorage()

name = form.getvalue("name")
surname = form.getvalue("surname")
tel = form.getvalue("tel")
ParentTel = form.getvalue("Parent-Tel")
address = form.getvalue("address")
email = form.getvalue("email")

cur = mydb.connection.cursor()
cur.execute("INSERT INTO students (name, surname, tel, ParentTel, address, email) VALUES (%s, %s, %s, %s, %s, %s)", (name, surname, tel, ParentTel, address, email))
mydb.commit()