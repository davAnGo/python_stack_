from flask import Flask, render_template 

app = Flask(__name__)    

@app.route('/play')          
def index():
    return render_template("index.html")  

@app.route('/play/<int:user_input>')
def index1(user_input):
    return render_template("index1.html",user_input = user_input)


@app.route('/play/<int:user_input>/<string:user_color>')
def index2(user_input, user_color):
    return render_template("index2.html",user_input = user_input, user_color = user_color)

if __name__=="__main__":   
    app.run(debug=True)