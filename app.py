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


@app.route('/submit', methods=['POST'])
def submit():
    data_srt = request.data.decode("utf-8")
    data = json.loads(data_srt)
    mesurement = Mesurement(temp=data['temp'],
                            light=data['light'],
                            wind_speed=data['wind'],
                            press=data['press'],
                            voltage=data['voltage'],
                            date=datetime.today()
                            )
    mesurement.save()
    return data_srt

if __name__ == '__main__':
    app.run(debug=True) #app.run()
