from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
app = Flask(__name__)

MONGO_URL = os.environ.get('MONGOLAB_URI')
print("MONGOLAB_URI", MONGO_URL)
if MONGO_URL:
  # Get client
  print("Connected with MONGO_URL")
  app.config['MONGOALCHEMY_CONNECTION_STRING'] = MONGO_URL
  app.config['MONGOALCHEMY_DATABASE'] = 'heroku_xzpnfqgh'
else:
  print("Connected with local")
  # Not on an app with the MongoHQ add-on, do some localhost action
  app.config['MONGOALCHEMY_DATABASE'] = 'library'

db = MongoAlchemy(app)

class Mesurement(db.Document):
    temp = db.FloatField()
    light = db.FloatField()
    wind_speed = db.FloatField()
    press = db.FloatField()
    date = db.DateTimeField()
    team = db.IntField()

class Clothes(db.Document):
    temp = db.FloatField()
    name = db.StringField()
    part_of_the_body = db.StringField()

class Signs(db.Document):
    text = db.StringField()
    date_s = db.DateTimeField()
    date_e = db.DateTimeField()

# class Analyzed(db.Document):
#     tempAV = db.FloatField()
#     illuminationAV = db.FloatField()
#     wind_speedAV = db.FloatField()
#     pressureAV = db.FloatField()
#     dateAV = db.DateTimeField()
