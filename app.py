from flask import Flask, request, send_from_directory
from models import Mesurement, Clothes
from datetime import datetime

import json
from bson import json_util
app = Flask(__name__)

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))
app.config['STATIC_FOLDER'] = 'templates'


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/Template/css', path)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/Template/js', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('templates/Template/img', path)
@app.route('/src/<path:path>')
def send_src(path):
    return send_from_directory('templates/Template/src', path)

@app.route('/team/<path:path>')
def send_MS(path):
    b = Mesurement.query.raw_output()
    b = b.descending(Mesurement.date).all()
    b = b.filter(Mesurement.team == path).limit(1).one()
    return send_from_directory('templates/team')


@app.route('/')
def index():

    a = Mesurement.query.raw_output()
    a = a.descending(Mesurement.date).limit(1).one()
    print('a = ', a)
    if(a['temp']<0):
        Z ='-'
    else:
        Z='+'

    template = env.get_template('Template/index.html')
    return template.render(Z=Z, mesurement = a)
    # return json.dumps(N, default=json_util.default)


 #  Функция, необходимая для выборки одежды из базы данных одежды
    # cloth = Clothes.query.raw_output()
    # cloth = cloth.all()
    # Date = Mesurement.query.raw_output()
    # Date = Date.descending(Mesurement.date).limit(1).one()
    # k=0.1
    # N=['','','','']
    # temp_f = Date['temp'] - (Date['wind_speed']*k)
    # Min = 100000
    # for element in cloth:
    #     T = element['temp'] - temp_f
    #     if(T<0):
    #         T = T*(-1)
    #     if(T<=Min):
    #         Min = T
    #         if(element['part_of_the_body'] == "body"):
    #             N[1] = element['name']
    #         if(element['part_of_the_body'] == "head"):
    #             N[0] = element['name']
    #         if(element['part_of_the_body'] == "legs"):
    #             N[2] = element['name']
    #         if(element['part_of_the_body'] == "Feet"):
    #             N[3] = element['name']





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

@app.route('/get_all_readings')
def get_all_testimony():

    readings = Mesurement.query.raw_output()
    readings = readings.all()


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


# создать четыре типа одежды: головной убор, торс, ноги, стопы на три сезона: -30, -15, +20


# @app.route('/get')
# def get():
#     data = Mesurement.query.raw_output()
#     data = data.filter(Mesurement.temp > 0).limit(1).one()
#
#     return json.dumps(data, default=json_util.default)




# @app.route('/get_cloths')
# def get_cloths():
#
#     cloth = Clothes.query.raw_output()
#     cloth = cloth.all()
#     Date = Mesurement.query.raw_output()
#     Date = Date.ascending(Mesurement.date).limit(1).one()
#     # print(Date, Date['temp'])
#
#     k=0.5
#     i=''
#     temp_f = Date['temp'] - (Date['wind_speed']*k)
#     Min = 100000
#     for element in cloth:
#         # print(element)
#         ST = element['temp']
#         T = ST - temp_f
#         if(T<0):
#             T = T*(-1)
#         if(T<Min):
#             Min = T
#             i = element['name']
#
#     return json.dumps(i, default=json_util.default)
#     # return ()
#
