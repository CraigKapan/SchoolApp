from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class AppForm(FlaskForm):
    Name = StringField('Name')
    Surname = StringField('Surname')
    Tel = StringField('Tel')
    ParentTel = StringField('ParentTel')
    Address = StringField('Address')
    Email = StringField('Email')
    Submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    message = StringField('message')
    submit = SubmitField('submit')