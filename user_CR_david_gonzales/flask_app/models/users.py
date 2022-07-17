import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL('users_schema').query_db(query, data)

    @staticmethod
    def validate_user(users):
        is_valid = True
        if len(users['first_name']) < 3:
            flash("First name must have at least 3 characters")
            is_valid = False
        if len(users['last_name']) < 2:
            flash("Last name must have at least 2 characters")
            is_valid = False
        if len(users['email']) < 1:
            flash("Email field may not be empty!")
            is_valid = False
        if not EMAIL_REGEX.match(users['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def remove_dups(cls, users):
        is_valid = True
        query = "SELECT email FROM users WHERE id > 0;"
        results = connectToMySQL('users_schema').query_db(query)
        emailAddresses = []
        for emails in results:
            if results[emails] == results[emails+1]:
                flash("Email is already registered")
                is_valid = False
            else:
                emailAddresses.append(cls(emails))
            return emailAddresses        
    