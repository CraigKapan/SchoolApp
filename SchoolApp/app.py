import cgi, mysql.connector
from flask import request

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
ParentTel = form.getvalue("ParentTel")
address = form.getvalue("address")
email = form.getvalue("email")

cur = mydb.cursor()
cur.execute("INSERT INTO schoolapptb (name, surname, tel, ParentTel, address, email) VALUES (%s, %s, %s, %s, %s, %s)", (name, surname, tel, ParentTel, address, email))
mydb.commit()

cur.close()
mydb.close()