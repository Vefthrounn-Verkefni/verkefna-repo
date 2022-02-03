from flask import Flask, render_template, request,redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
from forms import CreateUser
app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/test.db"
#db = SQLAlchemy(app)


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/create_user",methods=["GET","POST"])
def create_user():
    create_user = CreateUser()
    if create_user.validate_on_submit():
        print(create_user.username)
    return render_template("CreateUser.html",form=create_user)

if __name__ == "__main__":
    app.run(debug=True)