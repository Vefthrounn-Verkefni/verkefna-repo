from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class CreateUser(FlaskForm):
    username = TextAreaField("Username", validators = [Length(min=4, max=25)])
    email = TextAreaField("Email Address", validators = [Length(min=6, max=35)])
    password = TextAreaField("New Password", validators = [Length(min=6, max=35)])
    submit = SubmitField("Create User")
    