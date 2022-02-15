from flask import Flask, render_template, request,redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, login_required,login_user,LoginManager,logout_user,current_user
from forms import CreateUser, LoginForm


# Flask Uppseting
app = Flask(__name__)
app.config["SECRET_KEY"] = "password"

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
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "<Name %r>" % self.name

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
            name=signUpForm.name.data = ""
            username=signUpForm.username.data = ""
            email=signUpForm.email.data = ""
            flash("User added","success")

    return render_template("CreateUser.html",form=signUpForm)

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/") # gera custom page seinna

@app.errorhandler(500)
def page_not_found(e):
    return redirect("/") # gera custom page seinna

@app.errorhandler(401)
def page_not_found(e):
    flash("You Dont have premission to enter this page please log in","negative")
    return redirect("/login") 
if __name__ == "__main__":
    app.run(debug=True)
