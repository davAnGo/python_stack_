from flask import Flask , render_template

app = Flask(__name__)    

@app.route('/')          
def index():
    return render_template("index0.html")

@app.route('/<int:user_size>')
def size(user_size):
    return render_template('index1.html', user_size = user_size)

@app.route('/<int:user_sizeX>/<int:user_sizeY>')
def sizeXY(user_sizeX, user_sizeY):
    return render_template('index.html', user_sizeX = user_sizeX, user_sizeY = user_sizeY)


@app.route('/<int:user_sizeX>/<int:user_sizeY>/<string:user_color1>/<string:user_color2>')
def sizeAndColor(user_sizeX, user_sizeY,user_color1, user_color2):
    return render_template('index2.html', user_sizeX = user_sizeX, user_sizeY = user_sizeY, user_color1 = user_color1, user_color2 = user_color2)

if __name__=="__main__":   
    app.run(debug=True)    

