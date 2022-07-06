from flask import Flask, render_template,session, redirect

app = Flask(__name__)
app.secret_key = 'this key is very secret'

@app.route('/')
def index():
    if "addOne" not in session:
        session["addOne"] = 0
    else:
        session["addOne"] += 1
    return render_template('index.html')

@app.route('/clear')
def reset():
    session.clear()
    return redirect('/')

@app.route('/addTwo')
def addTwo():
    session['addOne'] +=1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
