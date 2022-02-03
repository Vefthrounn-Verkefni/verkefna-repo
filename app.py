from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")




@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)