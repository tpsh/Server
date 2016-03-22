from flask import Flask
from flask import request
import json
from models import Mesurement
from models import Sign
from models import Clothes
from bson import json_util

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))

app = Flask(__name__)

@app.route('/')
def index():
    template = env.get_template('mytemplate.html')
    return template.render()

@app.route('/get')
def hello():
    a = Mesurement.query.raw_output()
    a = a.filter(Mesurement.humidity > 7).all()
    b = Sign.query.raw_output()
    b = b.all()
    c = Clothes.query.raw_output()
    c = c.all()
    return json.dumps(c, default=json_util.default)

@app.route('/create')
def create():
    mesurement = Mesurement(temp=-8, ground_temp=1.5, light=2.33, wind_speed=12, wind_direction=0.33, pressure=4.53, humidity=8)
    mesurement.save()
    sign = Sign(sign='Звезды яркие - к хорошей погоде')
    sign.save()
    clothes = Clothes(temp=-7, name='Куртка и шапка')
    clothes.save()
    return 'created'

@app.route('/submit', methods=['POST'])
def submit():
    a = json.loads(request.data.decode("utf-8"))
    for i in a:
        mesuremsent = Mesurement(temp=i['temp'],
                                 ground_temp=i['ground_temp'],
                                 light=i['light'],
                                 wind_speed=i['wind_speed'],
                                 wind_direction=i['wind_direction'],
                                 pressure=i['pressure'],
                                 humidity=i['humidity'])
        mesuremsent.save()
    b = json.loads(request.data.decode("utf-8"))
    for i1 in b:
        sign = Sign(sign=i['sign'])
        sign.save()
    c = json.loads(request.data.decode("utf-8"))
    for i2 in c:
        clothes = Clothes(clothes=i['clothes'])

if __name__ == '__main__':
    app.run(debug=True)
