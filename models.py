from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'library'
db = MongoAlchemy(app)

class Mesurement(db.Document):
    temp = db.FloatField()
    illumination = db.FloatField()
    wind_speed = db.FloatField()
    pressure = db.FloatField()
    data = db.DateTimeField()
    team = db.IntField()

class Clothes(db.Document):
    temp = db.FloatField()
    name = db.StringField()
    part_of_the_body = db.StringField()

class Signs(db.Document):
    text = db.StringField()
    dateS = db.DateTimeField()
    dateF = db.DateTimeField()

# class Analyzed(db.Document):
#     tempAV = db.FloatField()
#     illuminationAV = db.FloatField()
#     wind_speedAV = db.FloatField()
#     pressureAV = db.FloatField()
#     dateAV = db.DateTimeField()
