from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import re
from secrets import compare_digest


def validateEmailDomain(form, field):
    allowedDomains = {".edu", ".ac.uk",".org"}
    isValid = False
    for domain in allowedDomains:
        if field.data.endswith(domain):
            isValid = True #stop once we found a valid email domain
            break

    if not isValid:
        raise ValidationError(f"Email must end with: {', '.join(allowedDomains)}")

def validateUsername(form, field): #checking for reserved usernames
    disallowedUsernames = {"admin", "root","superuser"}
    if field.data.lower() in disallowedUsernames:
        raise ValidationError(f"The username {field.data} is not allowed!")

def validatePassword(form, field):
    disallowedPasswords = {"password123", "admin", "123456", "qwerty", "letmein", "welcome", "iloveyou", "abc123", "monkey", "football"}
    hasUppercase = re.search(r"[A-Z]", field.data)
    hasLowercase = re.search(r"[a-z]", field.data)
    hasDigit = re.search(r"[0-9]", field.data)
    hasSpecial = re.search(r"[^A-Za-z0-9]", field.data) # ^ means not i.e. negated alphanumeric check

    for password in disallowedPasswords:
        if compare_digest(field.data, password):
            raise ValidationError("Password cannot be a common password")

    if form.email.data in field.data or form.name.data in field.data: #username/email in password check
        raise ValidationError("Password cannot contain your email or username!")

    if " " in field.data: #whitespace check
        raise ValidationError("Password cannot contain spaces!")

    if not(hasUppercase and hasLowercase and hasDigit and hasSpecial):
        raise ValidationError("Password must contain at least one uppercase letter, one lowercase letter, one digit or one special character!")

class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[
        DataRequired(message="Username is required."),
        Length(3, 30, message="Username must be between 3 and 30 characters"),
        validateUsername
    ])
    email = StringField('Email', validators=[
        DataRequired(message="Email is required."),
        Email(),
        validateEmailDomain
    ])
    password = PasswordField('Password', validators=[
        DataRequired("Password is required."),
        validatePassword,
        Length(12, message="Password must be at least 12 characters long.")
    ])
    confirmPassword = PasswordField('Confirm Password', validators=[
        DataRequired("Please confirm your password."),
        EqualTo('password')
    ])
    bio = StringField('Bio', validators=
    [DataRequired("Bio is required")
     ])
    submit = SubmitField('Register')