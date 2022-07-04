from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:user_input>')
def say(user_input):
    return f'Hi {user_input}!'

@app.route('/repeat/<int:user_int>/<string:user_input>')
def repeat(user_int,user_input):
    return f'{user_input * user_int}'

@app.route('/<string:user_input>')
def errorMessage(user_input):
    while user_input not in ['/','/dojo','/say/<string:user_input>','/repeat/<int:user_int>/<string:user_input>']:
        return 'Sorry! No response. Try again.'



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

