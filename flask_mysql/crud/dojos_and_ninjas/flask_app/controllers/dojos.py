from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect, flash
from flask_app import app

@app.route("/")
def index():
    return render_template('dojo_create.html')

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data={
        "name":request.form["name"]
    }
    Dojo.save(data)
    return redirect("/input/ninjas")

@app.route("/dojo_show" )
def read_dojo():
    return render_template("dojo_show.html", dojos = Dojo.get_all_dojos())


@app.route("/dojo/<int:id>/view")
def show_one_dojo(id):
    data = {
        "id":id
    }
    return render_template("show_one_dojo.html", this_dojo = Dojo.get_one_dojo())