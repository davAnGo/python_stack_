from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Recipe:
    
    #dont for get to adjust and change your db

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.thirty_min_or_less = data['thirty_min_or_less']
        self.created_at  = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @staticmethod  #validation set, can be used for editing as well
    def validate_recipe(form_data):
        is_valid = True
        print(form_data)
        #check name length
        if len(form_data['name'])<2:
            is_valid = False
            flash("Name must be 2 or more characters")
        #check description length
        if len(form_data['description'])<25:
            is_valid = False
            flash("Description must be at least 25 characters")
        #check instructions length
        if len(form_data['instructions'])<25:
            is_valid = False
            flash("Instructions must be at least 25 characters")

        #check bool of thirty min or less
        if "thirty_min_or_less" not in form_data:
            is_valid = False
            flash("Please select Yes or No")

        #check date
        if form_data['date_cooked'] == "":
            is_valid = False
            flash("Date is required")
        return is_valid


    @classmethod
    def save_recipe(cls, recipe_data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, thirty_min_or_less, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(thirty_min_or_less)s, %(user_id)s);"
        return connectToMySQL("recipes_db").query_db(query,recipe_data)

    @classmethod
    def edit_recipe(cls,recipe_data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, thirty_min_or_less = %(thirty_min_or_less)s WHERE id = %(id)s "
        return connectToMySQL("recipes_db").query_db(query,recipe_data)

    @classmethod
    def delete(cls,recipe_data):
        query = "DELETE FROM recipes WHERE id = %(id)s "
        return connectToMySQL("recipes_db").query_db(query,recipe_data)

    @classmethod
    def get_all_recipes_with_user(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL("recipes_db").query_db(query)
        if len(results) == 0: #check to see if there are any recipes in the database yet
            return[]#if not return an empty list
        else:
            recipes = [] 
            for recipe_dictionary in results:
                # create recipe object
                recipe_object = cls(recipe_dictionary) #cls() calls on the __init__ method inside this class
                #shared column names in tables will have to be changed ie table name added
                #grab user data linked to the recipe. 
                #not where the table name (users) has been added due to the two table sharing these names
                this_user_dictionary = {
                    "id" : recipe_dictionary['users.id'],
                    "first_name" : recipe_dictionary ['first_name'],
                    "last_name" : recipe_dictionary ['last_name'],
                    "email" : recipe_dictionary['email'],
                    "password" : recipe_dictionary['password'],
                    "created_at" : recipe_dictionary ['users.created_at'],
                    "updated_at" : recipe_dictionary['users.updated_at']
                }
                #create the User object
                user_object = user.User(this_user_dictionary)
                #link the user to the recipe
                recipe_object.user = user_object
                #add recipe to list of recipes
                recipes.append(recipe_object)
            return recipes

    @classmethod
    def get_one_recipe_with_user(cls,recipe_data):
        query = "SELECT * FROM recipes JOIN users ON recipes.id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL("recipes_db").query_db(query, recipe_data)
        if len(results) == 0: #check to see if there are any recipes in the database yet
            return None #this is none rather than an empty list because it is a max of one thing vs nothing
        else:
            # create recipe object
            recipe_object = cls(results[0]) #results['0'] represents the dictionary filled with recipe data at the index of 0 in the list "results"
            #shared column names in tables will have to be changed ie table name added
            #grab user data linked to the recipe. 
            #not where the table name (users) has been added due to the two table sharing these names
            this_user_dictionary = {
                "id" : results[0]['users.id'],
                "first_name" : results[0] ['first_name'],
                "last_name" : results[0] ['last_name'],
                "email" : results[0]['email'],
                "password" : results[0]['password'],
                "created_at" : results[0]['users.created_at'],
                "updated_at" : results[0]['users.updated_at']
            }
            #create the User object
            user_object = user.User(this_user_dictionary)
            #link the user to the recipe
            recipe_object.user = user_object
            #add recipe to list of recipes
            return recipe_object
