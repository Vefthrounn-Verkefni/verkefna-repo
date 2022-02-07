from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired,Length


class CreateUser(FlaskForm):
    name = StringField("Full Name",validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    email = StringField("Email",validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    



    