from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)])

    # TODO: Install 'email_validator' for email validation support
    email = StringField('Email',validators=[DataRequired(),Email()]) 
    # email = StringField('Email',validators=[DataRequired()]) 

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign')



class LoginForm(FlaskForm):
    # TODO: Install 'email_validator' for email validation support
    email = StringField('Email',validators=[DataRequired(),Email()])
    # email = StringField('Email',validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')