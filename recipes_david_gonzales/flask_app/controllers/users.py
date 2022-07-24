from flask_app import app
from flask_app.models.user import User 
from flask_app.models.recipe import Recipe
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)




#routes that take you to different pages
@app.route("/")
def index(): #this is the very beginning where the user can login or register
    return render_template("reg_log.html")

# invisible routes that add to database

@app.route("/register", methods = ['POST']) # a post route that registers a user by adding them to the database
def register_new_user():
    #start with validation
    if not User.validate(request.form):
        #if bad send user back to login
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)    
    #if good save to db and pass onto homepage
    user_data ={
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'],
    "password": pw_hash
    }
    user_id = User.save(user_data) #save to db
    session['user_id'] = user_id #save to session 
    return redirect("/dashboard")

@app.route("/login", methods = ['POST']) #post route that checks a users login info and lets them in or turns them away
def log_in_user():
    user_data = {"email" : request.form["email"]}
    registered_user = User.get_by_email(user_data)
    
    if not registered_user:
        flash("Invalid Email or Password")
        return redirect("/")

    if not bcrypt.check_password_hash(registered_user.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect("/")

    session['user_id'] = registered_user.id
    print("REGISTERED USER: ", registered_user.id)
    return redirect("/dashboard")


@app.route("/logout/user",methods = ['POST'])
def log_user_out():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard(): #the homepage of sorts that is the first stop after logging in
    if "user_id" not in session:
        return redirect("/")
    user_data = {
        'id':session['user_id']
    }
    print("USER_DATA",user_data['id'])
    return render_template("dashboard.html", user = User.get_user_by_id(user_data), recipes = Recipe.get_all_recipes_with_user()) #homepage is dashboard for reference








