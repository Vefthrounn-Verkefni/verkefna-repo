from email import message
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired,EqualTo,Length


class CreateUser(FlaskForm):
    name = StringField("Full Name",validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    email = StringField("Email",validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(),EqualTo("password2",message="Password must match")])
    password2 = PasswordField("Confirm Password",validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    
<<<<<<< HEAD
=======
    
>>>>>>> b2368efc24928e02e8c72c2403bbca619674efd2
