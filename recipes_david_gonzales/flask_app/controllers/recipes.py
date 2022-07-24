from pydoc import render_doc
from flask_app import app
from flask_app.models import user, recipe 
from flask import render_template, redirect, request, session, flash

@app.route("/add/recipe")
def add_recipe(): 
    # referencing session, make sure user is logged in in order to view this page
    if "user_id" not in session:
        return redirect("/")
        # make a data dictionary containing the session id 
    user_data = {
        'id':session['user_id']
    }
    # pass in the data dictionary to the method to get the user by said data and make it a variable
    
    # restate your variable as a variable because that is what it wants. You could also do the above step in the parentheses and skip this step
    return render_template("add_recipe.html", user = user.User.get_user_by_id(user_data)
)


@app.route("/save/recipe", methods = ['POST'])
def save_to_db():
    # referencing session, make sure user is logged in in order to view this page
    if "user_id" not in session:
        return redirect("/")
    #validate the recipe using a static method in the recipe model
    if not recipe.Recipe.validate_recipe(request.form): #fail sends you back 
        return redirect("/add/recipe")#to this form

        #create a data dictionary to get all the attributes form the form just filled out to put in the save method
    recipe_data ={
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date_cooked":request.form['date_cooked'],
        "thirty_min_or_less":request.form['thirty_min_or_less'],
        "user_id": session['user_id']
    }
        #add recipe to db with a class method through the recipes model sending in the dictionary as an argument

    recipe.Recipe.save_recipe(recipe_data)
    
    #finally get sent back to the dashboard to view your new recipe
    return redirect("/dashboard")



@app.route("/edit/recipe/<int:id>")
def edit_recipe_page(id):
    if "user_id" not in session:
        return redirect("/")
    recipe_data = {
        'id':id
    }
    return render_template("edit_recipe.html", this_recipe = recipe.Recipe.get_one_recipe_with_user(recipe_data))
    

@app.route("/edit/recipe/<int:id>", methods=['POST'])
def edit_recipe_in_db(id):
    if "user_id" not in session:
        return redirect("/")
#validate the recipe edits using a static method in the recipe model
    if not recipe.Recipe.validate_recipe(request.form): #fail sends you back 
        return redirect(f"/edit/recipe/{id}")#to this form
    #edit the team in the database
    recipe_data ={
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date_cooked":request.form['date_cooked'],
        "thirty_min_or_less":request.form['thirty_min_or_less'],
        "id":id
    }
    recipe.Recipe.edit_recipe(recipe_data)
    return redirect("/dashboard")

#to delete a recipe
@app.route("/recipe/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        return redirect("/")
    recipe_data = {
        'id':id
    }
    recipe.Recipe.delete(recipe_data)
    return redirect("/dashboard")


#view one recipe
@app.route("/recipe/<int:id>")
def read_recipe(id): #pass in the id from the int above
    if "user_id" not in session:#make sure someone not logged in cant get in
        return redirect("/")
        #data dictionary for the id of the recipe not the user. This will not be found in session
    recipe_data = {
        'id':id
    }
    return render_template("read_recipe.html", this_recipe = recipe.Recipe.get_one_recipe_with_user(recipe_data) )
    

    


