from flask import render_template, request, session, redirect, flash

from flask_app.models.users import User
from flask_app import app

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("create.html", users = users)

@app.route("/create_user", methods=["POST"])
def create_user():
    data ={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    if not User.validate_user(request.form):
        return redirect ('/')
    User.save(data)
    return redirect("/read")

@app.route("/read")
def read():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", users = users)


            