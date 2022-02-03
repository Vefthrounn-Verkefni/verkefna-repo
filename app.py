from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "password"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/test.db"
db = SQLAlchemy(app)


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")