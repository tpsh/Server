from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'library'
db = MongoAlchemy(app)

class Mesurement(db.Document):
    temp = db.FloatField()
    ground_temp = db.FloatField()
    light = db.FloatField()
    wind_speed = db.FloatField()
    wind_direction = db.FloatField()
    pressure = db.FloatField()
    humidity = db.FloatField()
