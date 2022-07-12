from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect, flash
from flask_app import app


@app.route('/input/ninjas')
def input_ninjas():
    return render_template('ninja_create.html', dojos = Dojo.get_all_dojos())



@app.route("/create/ninja", methods=['POST'])
def input_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id': request.form['dojos_id']
    }
    Ninja.save(data)
    return redirect('/list/ninjas')

@app.route("/list/ninjas")
def view_ninjas():

    return render_template("ninja_show.html",ninjas = Ninja.get_all() )    


