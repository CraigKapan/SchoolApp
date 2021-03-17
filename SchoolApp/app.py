from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'schoolappdb'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('application.html', students=data )
app.run()


@app.route('/add', methods = ['POST'])
def add():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))

 

if __name__ == "__main__":
    app.run(debug=True)






















































#!C:\Users\Craig\AppData\Local\Programs\Python\Python39-32\python.exe
# print("content-type:text/html\r\n\r\n")

# import cgi, mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="schoolappdb"
# )

# form = cgi.FieldStorage()

# Name = form.getvalue("Name")
# Surname = form.getvalue("Surname")
# Tel = form.getvalue("Tel")
# ParentTel = form.getvalue("ParentTel")
# Address = form.getvalue("Address")
# Email = form.getvalue("Email")

# cur = mydb.cursor()
# cur.execute("INSERT INTO schoolapptb (Name, Surname, Tel, ParentTel, Address, Email) VALUES (%s, %s, %s, %s, %s, %s)", (Name, Surname, Tel, ParentTel, Address, Email))
# mydb.commit()

# cur.close()
# mydb.close()