from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CreateUser
app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240))
    email = db.Column(db.String(385))
    password = db.Column(db.String(240))


    def __str__(self):
        return f"{self.id},{self.name} {self.email}"


@app.route("/",methods=["GET","POST"])
def index():
    users = UserModel.query.all()
    return render_template("index.html", users=users)

@app.route("/create_user",methods=["GET","POST"])
def create_user():
    create_user = CreateUser()
    if create_user.validate_on_submit():
        newUser = UserModel(name=create_user.name.data,email=create_user.email.data,password=create_user.password.data)
        db.session.add(newUser)
        db.session.commit()
    return render_template("CreateUser.html",form=create_user)

if __name__ == "__main__":
    app.run(debug=True)