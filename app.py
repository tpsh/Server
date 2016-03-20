from flask import Flask
from flask import request
from models import Mesurement
import json
from bson import json_util
app = Flask(__name__)

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))

@app.route('/')
def index():
    a = Mesurement.query.raw_output()
    a = a.filter(Mesurement.humidity > 3).all()
    template = env.get_template('MyTemplate.html')
    return template.render()

@app.route('/create')
def create():
    mesuremsent = Mesurement(temp=14, ground_temp=7, light=0.55, wind_speed=30, wind_direction=0.45, pressure=7, humidity=2)
    mesuremsent.save()
    return 'created'

@app.route('/get')
def get():
    data = Mesurement.query.raw_output()
    data = data.filter(Mesurement.temp > 10).all()


    return json.dumps(data, default=json_util.default)



@app.route('/submit', methods=['POST'])
def submit():
    data = json.loads(request.data.decode("utf-8"))
    for element in data:
        mesuremsent = Mesurement(temp=i['temp'],
                                 ground_temp=i['ground_temp'],
                                 light=i['light'],
                                 wind_speed=i['wind_speed'],
                                 wind_direction=i['wind_direction'],
                                 pressure=i['pressure'],
                                 humidity=i['humidity'])
        mesuremsent.save()

    return "saved"



if __name__ == '__main__':
    app.run(debug=True) #app.run()
