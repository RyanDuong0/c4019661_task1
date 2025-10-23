from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[
        DataRequired(message="Username is required."),
        Length(3, 30, message="Username must be between 3 and 30 characters")
    ])
    email = StringField('Email', validators=[DataRequired(message="Email is required."), Email()])
    password = PasswordField('Password', validators=[DataRequired("Password is required.")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired("Please confirm your password."), EqualTo('password')])
    bio = StringField('Bio', validators=[DataRequired()])
    submit = SubmitField('Register')
