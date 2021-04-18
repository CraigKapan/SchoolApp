from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField

class AppForm(FlaskForm):
    Name = StringField('Name')
    Surname = StringField('Surname')
    Tel = StringField('Tel')
    ParentTel = StringField('ParentTel')
    Address = StringField('Address')
    Email = StringField('Email')
    Image = FileField('Image')
    Birth_Certificate = FileField('Birth_Certificate')
    Id_Number = StringField('Id_Number')
    Submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    message = StringField('message')
    submit = SubmitField('submit')

class Adminform(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')