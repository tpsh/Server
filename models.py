from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
import os
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

  # mongodb://<dbuser>:<dbpassword>@ds021299.mlab.com:21299/heroku_xzpnfqgh
class Mesurement(db.Document):
    temp = db.FloatField()
    light = db.FloatField()
    wind_speed = db.FloatField()
    press = db.FloatField()
    voltage = db.FloatField()
    team = db.IntField()
    date = db.DateTimeField()    
