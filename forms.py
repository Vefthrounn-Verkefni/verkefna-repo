from email import message
from optparse import Values
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
    
class EditUser(FlaskForm):
    name = StringField("Full Name",validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    email = StringField("Email",validators = [DataRequired()])
    bio = StringField("Bio",validators = [DataRequired()])