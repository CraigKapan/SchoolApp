import tkinter
from tkinter import messagebox

import mysql.connector
import win32api
from flask import Flask, redirect, render_template, request, url_for

from forms import Adminform, AppForm, ContactForm

root = tkinter.Tk()
root.withdraw()


app = Flask(__name__)


app.config['SECRET_KEY'] = '12345'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="schoolappdb"
)
mycursor = mydb.cursor()
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    cform = ContactForm()
    if cform.is_submitted():
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        mycursor.execute("INSERT INTO contact_table (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        mydb.commit()
        return redirect(url_for('index'))
    return render_template('contact.html', form=cform)

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
        return redirect(url_for('index'))
    return render_template('application.html', form=form)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    mycursor.execute("SELECT * FROM contact_table, schoolapptb")
    data = mycursor.fetchall()
    return render_template('admin.html', contact_table = data, schoolapptb = data)

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    aform = Adminform()
    Email = request.form['Email']
    Password = request.form['Password']
    if len(Password) < 7:
        win32api.MessageBox(0, 'Password input is wrong', 'Error')
        return redirect(url_for('index'))

    if len(Password) > 7:
        win32api.MessageBox(0, 'Password input is wrong', 'Error')
        return redirect(url_for('index'))

    if len(Password) == 7 and Password == '$@Admin': 
        return redirect(url_for('admin'))

    if len(Password) == 7 and Password != '$@Admin':
        win32api.MessageBox(0, 'Password input is wrong', 'Error')
        return redirect(url_for('index'))




    if len(Email) < 15:
        win32api.MessageBox(0, 'Email input is wrong', 'Error')
        return redirect(url_for('index'))

    if len(Email) > 15:
        win32api.MessageBox(0, 'Email input is wrong', 'Error')
        return redirect(url_for('index'))

    if len(Email) == 15 and Email == 'Admin@gmail.com': 
        return redirect(url_for('admin'))

    if len(Email) == 15 and Email != 'Admin@gmail.com':
        win32api.MessageBox(0, 'Email input is wrong', 'Error')
        return redirect(url_for('index'))

    return render_template('application.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
