from flask import Flask
from flask import request
from datetime import datetime
from dateutil.parser import parse
import json
from babel import dates
# import pandas as pd
# from bson import json_util
from models import Mesurement

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))
def format_datetime(value, format='medium'):
    print(value)
    value = parse(str(value))

    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return dates.format_datetime(value, format, tzinfo=dates.get_timezone('Asia/Vladivostok'))

env.filters['datetime'] = format_datetime
app = Flask(__name__)


@app.route('/')
def index():
    a = Mesurement.query.raw_output()
    a = a.ascending('date').limit(20)
    template = env.get_template('mytemplate.html')
    return template.render(mesurements=a)

# @app.route('/pandas')
# def pandas():
#     a = Mesurement.query.raw_output()
#     a = a.all()
#     df = pd.DataFrame(list(a))
#     print(df.head())
#     template = env.get_template('mytemplate.html')
#     return template.render(mesurements=a)


@app.route('/submit', methods=['POST'])
def submit():
    data_srt = request.data.decode("utf-8")
    data = json.loads(data_srt)
    mesurement = Mesurement(temp=data['temp'],
                            light=data['light'],
                            wind_speed=data['wind'],
                            press=data['press'],
                            voltage=data['voltage'],
                            team=data['team'],
                            date=datetime.today()
                            )
    mesurement.save()
    return data_srt

if __name__ == '__main__':
    app.run(debug=True) #app.run()
