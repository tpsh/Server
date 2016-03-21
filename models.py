from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
import os
app = Flask(__name__)


MONGO_URL = os.environ.get('MONGOHQ_URL')
if MONGO_URL:
  # Get client
  app.config['MONGOALCHEMY_CONNECTION_STRING'] = MONGO_URL
  app.config['MONGOALCHEMY_DATABASE'] = 'heroku_xzpnfqgh'
else:
  # Not on an app with the MongoHQ add-on, do some localhost action
  app.config['MONGOALCHEMY_DATABASE'] = 'library'


db = MongoAlchemy(app)

  # mongodb://<dbuser>:<dbpassword>@ds021299.mlab.com:21299/heroku_xzpnfqgh
class Mesurement(db.Document):
    temp = db.FloatField()
    ground_temp = db.FloatField()
    light = db.FloatField()
    wind_speed = db.FloatField()
    wind_direction = db.FloatField()
    pressure = db.FloatField()
    humidity = db.FloatField()
