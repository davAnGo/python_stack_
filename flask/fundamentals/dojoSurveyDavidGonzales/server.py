from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'this is a very secret key'

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/results')
def showFormData():
    return render_template ("results.html")

@app.route('/take_survey', methods=["POST"])
def take_survey():
    session['full_name']= request.form['full_name']
    session['my_location']= request.form['my_location']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    return redirect('/results')


if __name__ =="__main__":
    app.run(debug = True)