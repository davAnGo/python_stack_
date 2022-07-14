from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.fav_lang = data['fav_lang']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_survey_data(cls):
        query = "SELECT * FROM survey_data ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL("dojo_survey_db").query_db(query)
        print(results[0])
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO survey_data (name, location, fav_lang, comments) VALUES (%(name)s, %(location)s, %(fav_lang)s, %(comments)s);"
        return connectToMySQL('dojo_survey_db').query_db(query,data)
        
    @staticmethod 
    def is_valid(survey):
        is_valid = True
        if len(survey['name'])<3:
            is_valid = False
            flash("Name must be at least 3 Letters")
        if len(survey['location']) <1:
            is_valid = False 
            flash("Must select at least one location")
        if len(survey['fav_lang'])<1:
            is_valid = False
            flash("Must select at least one language")
        if len(survey['comments']) <5:
            is_valid = False
            flash("Comment must be at least 5 characters")
        return is_valid
