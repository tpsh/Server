# from flask import Flask
# from flask.ext.mongoalchemy import MongoAlchemy
# app = Flask(__name__)
# app.config['MONGOALCHEMY_DATABASE'] = 'library'
# db = MongoAlchemy(app)
#
# class Mesurement(db.Document):
#     temp = db.FloatField()
#     illumination = db.FloatField()
#     wind_speed = db.FloatField()
#     pressure = db.FloatField()
#     date = db.DateTimeField()
#
# class Clothes(db.Document):
#     temp = db.FloatField()
#     name = db.StringField()
#     part_of_the_body = db.StringField()
