from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re # must be imported to pattern validate email
from flask_bcrypt import Bcrypt #lets make sure our passwords stay safe by importin Bcrypt
bcrypt = Bcrypt(app)



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    
    #dont for get to adjust and change your db

    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at  = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

        #validation
    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name'])<2:
            is_valid = False
            flash("First Name must have more than 2 characters")
        if len(user_data['last_name'])<2:
            is_valid = False
            flash("Last Name must have more than 2 characters")
        if not EMAIL_REGEX.match(user_data['email']):
            is_valid = False
            flash("Invalid email address.")            
        if len(user_data['password'])<8:
            is_valid = False
            flash("Password must contain at least 8 characters")
        if user_data['password'] != user_data['confirm']:
            is_valid = False
            flash("Passwords do not match.")
        return is_valid
    

    
    @classmethod
    def save(cls, user_data):
        query ="INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s,%(last_name)s, %(email)s, %(password)s, NOW(),NOW() );"
        return connectToMySQL("recipes_db").query_db(query, user_data)

    @classmethod
    def get_by_email(cls, user_data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipes_db").query_db(query,user_data)

        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls, user_data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("recipes_db").query_db(query,user_data)
        return cls(result[0])