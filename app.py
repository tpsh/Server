from flask import Flask
from flask import request
from datetime import datetime
import json
# from bson import json_util
from models import Mesurement

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))

app = Flask(__name__)


@app.route('/')
def index():
    a = Mesurement.query.raw_output()
    a = a.all()
    template = env.get_template('mytemplate.html')
    return template.render(mesurements=a)

# @app.route('/get')
# def hello():
#     a = Mesurement.query.raw_output()
#     a = a.filter(Mesurement.humidity > 3).all()
#
#     return json.dumps(a, default=json_util.default)

@app.route('/create')
def create():
    mesurement = Mesurement(temp=2,
                            ground_temp=2.5,
                            light=0.33,
                            wind_speed=22,
                            wind_direction=0.33,
                            pressure=5,
                            humidity=5
                            )
    mesurement.save()
    return 'created'

# @app.route('/submit_get')
# def submit_get():
#     return json.dumps(request.args)

@app.route('/submit', methods=['POST'])
def submit():
    print(request.data)
    # data_srt = request.data.decode("utf-8")
    # data = json.loads(data_srt)
    # mesurement = Mesurement(temp=data['temp'],
    #                         light=data['light'],
    #                         wind_speed=data['wind'],
    #                         press=data['press'],
    #                         date=datetime.today()
    #                         )
    # mesurement.save()
    # return data_srt
    return ""

if __name__ == '__main__':
    app.run(debug=True) #app.run()
