from xml.dom import ValidationErr

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

def validateEmailDomain(form, field):
    allowedDomains = {".edu", ".ac.uk",".org"}

def validateUsername(form, field): #checking for reserved usernames
    disallowedUsernames = {"admin", "root","superuser"}
    if field.data.lower() in disallowedUsernames:
        raise ValidationError(f"The username {field.data} is not allowed!")

class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[
        DataRequired(message="Username is required."),
        Length(3, 30, message="Username must be between 3 and 30 characters"),
        validateUsername
    ])
    email = StringField('Email', validators=[DataRequired(message="Email is required."), Email()])
    password = PasswordField('Password', validators=[DataRequired("Password is required.")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired("Please confirm your password."), EqualTo('password')])
    bio = StringField('Bio', validators=[DataRequired("Bio is required")])
    submit = SubmitField('Register')

