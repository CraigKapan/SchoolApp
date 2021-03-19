from flask import Flask, render_template, redirect, request, url_for
from forms import AppForm
import mysql.connector

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="schoolappdb"
)
mycursor = mydb.cursor()
@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = AppForm()
    if form.is_submitted():
        Name = request.form['Name']
        Surname = request.form['Surname']
        Tel = request.form['Tel']
        ParentTel = request.form['ParentTel']
        Address = request.form['Address']
        Email = request.form['Email']
        mycursor.execute("INSERT INTO schoolapptb (Name, Surname, Tel, ParentTel, Address, Email) VALUES (%s, %s, %s, %s, %s, %s)", (Name, Surname, Tel, ParentTel, Address, Email))
        mydb.commit()
        return redirect(url_for('apply'))
    return render_template('application.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()