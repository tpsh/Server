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
    date = db.DateTimeField()
    team = db.IntegerFiled

class Clothes(db.Document):
    temp = db.FloatField()
    name = db.StringField()
    part_of_the_body = db.StringField()

# class Analyzed(db.Document):
#     tempAV = db.FloatField()
#     illuminationAV = db.FloatField()
#     wind_speedAV = db.FloatField()
#     pressureAV = db.FloatField()
#     dateAV = db.DateTimeField()

class Signs(db.Document):
    text = db.StringField()
