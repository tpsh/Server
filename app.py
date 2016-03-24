from flask import Flask
from flask import request
# from models import Mesurement, Clothes
from datetime import datetime

import json
# from bson import json_util
app = Flask(__name__)

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))

@app.route('/')
def index():
    # a = Mesurement.query.raw_output()
    # a = a.filter(Mesurement.temp > 3).all()
    template = env.get_template('index.html')
    return template.render()

@app.route('/create')
def create():
    mesuremsent = Mesurement(temp=14, illumination=0.55, wind_speed=30, pressure=7)
    mesuremsent.save()
    return 'created'

@app.route('/create_cloths')
def create_cloths():
    clothes = Clothes(name="Bolonki", temp= -30, part_of_the_body = "legs")
    clothes.save()
    return 'Сlothing created'


@app.route('/get')
def get():
    data = Mesurement.query.raw_output()
    data = data.filter(Mesurement.temp > 0).limit(1).one()



    return json.dumps(data, default=json_util.default)

@app.route('/get_cloths')
def get_cloths():
    cloth = Clothes.query.raw_output()
    cloth = cloth.all()

    Date = Mesurement.query.raw_output()
    Date = Date.ascending(Mesurement.date).limit(1).one()
    print(Date, Date['temp'])


    k=0.5
    temp_f = Date['temp'] - (Date['wind_speed']*k)
    Min = 100000
    for element in cloth:
        # print(element)
        ST = element['temp']
        T = ST - temp_f
        if(T<0):
            T = T*(-1)
        if(T<Min):
            Min = T
            C = element['name']

    return json.dumps(C, default=json_util.default)
    # return ()


@app.route('/submit', methods=['POST'])
def submit():
    data = json.loads(request.data.decode("utf-8"))

    for element in data:
        mesuremsent = Mesurement(temp = element['temp'],
                                 illumination = element['illumination'],
                                 wind_speed = element['wind_speed'],
                                 pressure = element['pressure'],
                                 date = datetime.today())
        mesuremsent.save()

    return "saved"



if __name__ == '__main__':
    app.run(debug=True) #app.run()
