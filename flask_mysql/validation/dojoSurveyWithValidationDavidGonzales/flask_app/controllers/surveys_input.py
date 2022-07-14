from flask_app import app
from flask import render_template, redirect, request, session, flash 
from flask_app.models.survey import Survey



@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/results')
def showFormData():
    print(type(Survey.get_survey_data().name))
    return render_template ("results.html", survey = Survey.get_survey_data())

@app.route('/take_survey', methods=["POST"])
def take_survey():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/results')
    return redirect('/')
