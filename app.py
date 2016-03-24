from flask import Flask
from flask import request
from models import Mesurement, Clothes
from datetime import datetime

import json
from bson import json_util
app = Flask(__name__)

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates/Template'))
app.config['STATIC_FOLDER'] = 'templates/Template'

@app.route('/')
def index():
    # a = Mesurement.query.raw_output()
    # a = a.filter(Mesurement.temp > 3).all()


    cloth = Clothes.query.raw_output()
    cloth = cloth.all()
    Date = Mesurement.query.raw_output()
    Date = Date.descending(Mesurement.date).limit(1).one()

    k=0.1
    N=['','','','']
    temp_f = Date['temp'] - (Date['wind_speed']*k)
    Min = 100000

    for element in cloth:
        T = element['temp'] - temp_f
        if(T<0):
            T = T*(-1)
        if(T<=Min):
            Min = T
            if(element['part_of_the_body'] == "body"):
                N[1] = element['name']
            if(element['part_of_the_body'] == "head"):
                N[0] = element['name']
            if(element['part_of_the_body'] == "legs"):
                N[2] = element['name']
            if(element['part_of_the_body'] == "Feet"):
                N[3] = element['name']
    template = env.get_template('index.html')

    # return json.dumps(N, default=json_util.default)
    return template.render()
    # for element in cloth:
    #      print(element)
    #     ST = element['temp']
    #     T = ST - temp_f
    #     if(T<0):
    #         T = T*(-1)
    #     if(T<Min):
    #         Min = T
    #         i = element['name']


    # template = env.get_template('MyTemplate.html')


@app.route('/create')
def create():
    mesuremsent = Mesurement(temp=14, illumination=0.55, wind_speed=30, pressure=7)
    mesuremsent.save()
    return 'created'

@app.route('/create_cloths')
def create_cloths():
    clothes = Clothes(name="Sandali", temp = 20, part_of_the_body = "Feet")
    clothes.save()
    return 'Сlothing created'
# создать четыре типа одежды: головной убор, торс, ноги, стопы на три сезона: -30, -15, +20
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
    i=''
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
            i = element['name']

    return json.dumps(i, default=json_util.default)
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
