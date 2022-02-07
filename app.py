from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CreateUser
from datetime import datetime
app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime,default=datetime.utcnow())


    def __repr__(self):
        return "<Name %r>" % self.name


@app.route("/",methods=["GET","POST"])
def index():
    users = UserModel.query.all()
    return render_template("index.html", users=users)

@app.route("/create_user",methods=["GET","POST"])
def create_user():
    create_user = CreateUser()
    if create_user.validate_on_submit():
        pass
    return render_template("CreateUser.html",form=create_user)

if __name__ == "__main__":
    app.run(debug=True)