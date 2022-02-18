from json.encoder import py_encode_basestring_ascii
from flask import Flask, render_template, request,redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, login_required,login_user,LoginManager,logout_user,current_user
from forms import CreateUser, LoginForm,EditUser
from werkzeug.utils import secure_filename
import uuid as uuid
import os

# Flask Uppseting
app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
UPLOAD_FOLDER = "static/profile_data/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Sqlalchemy uppsetning
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password123@localhost/flask_database"
db = SQLAlchemy(app)

# Flask Login uppsetning
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

# SQL model fyrir User
class UserModel(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    bio = db.Column(db.String(400), nullable=False,default="")
    profile_picture = db.Column(db.String(400),default="n/a")
    date_added = db.Column(db.DateTime,default=datetime.utcnow())
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return "<Name %r>" % self.name
""" 
class ClothingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    describtion = db.Column(db.String(220))
    type = db.Column(db.String(10), nullable=False)
    image_link = db.Column(db.String(),nullable=False)
"""
@app.route("/",methods=["GET","POST"])
def index():
    users = UserModel.query.all()
    return render_template("index.html",users=users)

@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():
    return render_template("userDashboard.html",)

@app.route("/login",methods=["GET","POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = UserModel.query.filter_by(username=loginForm.username.data).first()
        if user:
            if check_password_hash(user.password_hash,loginForm.password.data):
                login_user(user)
                flash("Logged In","success")
                return redirect(url_for("dashboard"))
            else: 
                flash("Incorrect password","negative")
        else:
            flash(f"User {loginForm.username.data} doesn't exist","negative")

    return render_template("login.html",form=loginForm)

@app.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You Have Logged out","blue")
    return redirect(url_for("index"))

@app.route("/create_user",methods=["GET","POST"])
def create_user():
    signUpForm = CreateUser()
    if signUpForm.validate_on_submit():
        userEmail = UserModel.query.filter_by(email=signUpForm.email.data).first() 
        userUsername = UserModel.query.filter_by(username=signUpForm.username.data).first() 
        if userEmail:
            flash("Email in use","yellow")
        if userUsername:
            flash("Username in use","yellow")
        if userUsername  == None and userEmail == None:
            hashed_password = generate_password_hash(signUpForm.password.data,"sha256")
            user = UserModel(   name=signUpForm.name.data,
                                username=signUpForm.username.data,
                                email=signUpForm.email.data,
                                password_hash = hashed_password
                            )
            db.session.add(user)
            db.session.commit()
            path = os.path.join(app.config["UPLOAD_FOLDER"],f"{user.id}_{user.username}")
            os.mkdir(path)
            name=signUpForm.name.data = ""
            username=signUpForm.username.data = ""
            email=signUpForm.email.data = ""

            flash("User added","success")
            login_user(user)

            return redirect("dashboard")

    return render_template("CreateUser.html",form=signUpForm)

@app.route("/editUser",methods=["GET","POST"])
@login_required
def edit_user():
    edit_userForm = EditUser()
    if edit_userForm.validate_on_submit():
        logged_user = UserModel.query.get(current_user.id)
        logged_user.id  = current_user.id
        logged_user.username = edit_userForm.username.data
        logged_user.name = edit_userForm.name.data
        logged_user.email = edit_userForm.email.data
        logged_user.bio = edit_userForm.bio.data
        if edit_userForm.profile_picture != None:
            profile_pic = edit_userForm.profile_picture.data
            pic_filename = secure_filename(profile_pic.filename)
            pic_name = str(uuid.uuid1()) + "_" + pic_filename
            profile_pic.save(os.path.join(app.config["UPLOAD_FOLDER"]+str(current_user.id)+"_"+str(current_user.username),pic_name))
            logged_user.profile_picture = pic_name
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("userSettings.html",form=edit_userForm)

@login_required
def logout():
    logout_user()
    flash("You Have Logged out","blue")
    return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/") # gera custom page seinna


@app.route("/whatToWear")
def whatToWear():
    return render_template("whatShouldWear.html")

@app.errorhandler(500)
def page_not_found(e):
    return redirect("/") # gera custom page seinna

@app.errorhandler(401)
def page_not_found(e):
    flash("You Dont have premission to enter this page please log in","negative")
    return redirect("/login") 
if __name__ == "__main__":
    app.run(debug=True)
