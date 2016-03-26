from flask import Flask, request, send_from_directory
from models import Mesurement, Clothes, Signs
from datetime import datetime
from Analyze import FindMean

import json
from dateutil.parser import parse
from babel import dates
from bson import json_util
app = Flask(__name__)


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
app.config['STATIC_FOLDER'] = 'templates'
env.filters['jsonify'] = json.dumps

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('templates/img', path)
@app.route('/src/<path:path>')
def send_src(path):
    return send_from_directory('templates/src', path)
@app.route('/team/<team_id>')
def send_MS(team_id):
    b = Mesurement.query.raw_output()
    b = b.filter(Mesurement.team == int(team_id)).all()
    template = env.get_template('team.html')
    return template.render(data=b, team=team_id)

@app.route('/')
def index():
    a = Mesurement.query.raw_output()
    a = a.descending(Mesurement.date).limit(3)
    z = a
    Average = FindMean(z)

    b = Signs.query.raw_output()
    b = b.all()
    ok = []
    print(int(datetime.today().day))
    for element in b:
        if((element['date_s'].month<=datetime.today().month) and (element['date_e'].month>=datetime.today().month)):
            if((element['date_s'].day<=datetime.today().day) and (element['date_e'].day>=datetime.today().day)):
                ok.append(element)
    # sign = b.['text']
    template = env.get_template('index.html')
    # return json.dumps(ok, default=json_util.default)
    week = [{
        "temp" : 6,
        "wind_speed" : 3
    },{
        "temp" : 5,
        "wind_speed" : 10
    },{
        "temp" : 7,
        "wind_speed" : 18
    },{
        "temp" : 9,
        "wind_speed" : 4
    },{
        "temp" : 8,
        "wind_speed" : 1
    },{
        "temp" : 7,
        "wind_speed" : 5
    },{
        "temp" : 10,
        "wind_speed" : 2
    }]
    Average['temp'] = int(Average['temp'])
    return template.render(mesurement = Average, sign = {}, week = week) #sign

@app.route('/top')
def top():
    a = Mesurement.query.raw_output()
    a = a.descending('date').limit(20)
    template = env.get_template('top.html')
    return template.render(mesurements=a)


@app.route('/csv')
def csv():
    a = Mesurement.query.raw_output()
    a = a.descending('date')
    template = env.get_template('csv.html')
    return template.render(mesurements=a)

@app.route('/table')
def table():
    a = Mesurement.query.raw_output()
    a = a.descending('date')
    template = env.get_template('table.html')
    return template.render(mesurements=a)

@app.route('/create_signs')
def create_signs():
    a = [
    {
     "text" : "Если осенью березы желтеют с верхушки, следующая весна будет ранняя, а если снизу, то поздняя",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
     "text" : "Листопад прошел быстро – скоро наступит стужа и зима будет суровой, а если листья остаются зелеными и долго держатся на деревьях – зима будет короткая, с небольшими морозами",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
     "text" : "Осень будет теплой, если до поздней осени цветут анютины глазки, лютики, маргаритки, тысячелистник, клевер",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "Осенью птицы летят низко – к холодной, высоко – к теплой зиме",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "В лесу много рябины – осень будет дождливая, мало – сухая",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "Теплая осень – к долгой зиме",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "Гром в сентябре предвещает теплую осень",
     "date_s" :  datetime.strptime('0109', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "В этот день собирали рябину и калину. Хороший урожай рябины – к морозу.",
     "date_s" :  datetime.strptime('1809', "%d%m"),
     "date_e" :  datetime.strptime('1809', "%d%m")
    },
    {
    "text" : "Этот день считается началом бабьего лета. Если первый день бабьего лета ясный, то бабье лето будет теплым и солнечным.",
     "date_s" :  datetime.strptime('1409', "%d%m"),
     "date_e" :  datetime.strptime('1409', "%d%m")
    },
    {
    "text" : "Много паутины на бабье лето – к ясной осени и холодной зиме.",
     "date_s" :  datetime.strptime('0106', "%d%m"),
     "date_e" :  datetime.strptime('3108', "%d%m")
    },
    {
    "text" : "Если из березы течет много сока – то лето будет дождливым",
     "date_s" :  datetime.strptime('0106', "%d%m"),
     "date_e" :  datetime.strptime('3108', "%d%m")
    },
    {
    "text" : "Если кукушка кукует на сухом дереве – ждите морозов",
     "date_s" :  datetime.strptime('0106', "%d%m"),
     "date_e" :  datetime.strptime('3108', "%d%m")
    },
    {
    "text" : "Орехов много, грибов мало – зима будет снежная и суровая.",
     "date_s" :  datetime.strptime('0108', "%d%m"),
     "date_e" :  datetime.strptime('3108', "%d%m")
    },
    {
    "text" : "Осенний иней – к сухой и солнечной погоде, к теплу",
     "date_s" :  datetime.strptime('2510', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "Появились комары поздней осенью – к мягкой зиме",
     "date_s" :  datetime.strptime('2510', "%d%m"),
     "date_e" :  datetime.strptime('3011', "%d%m")
    },
    {
    "text" : "Когда птицы гнезда вьют на солнечной стороне – будет холодное лето",
     "date_s" :  datetime.strptime('1003', "%d%m"),
     "date_e" :  datetime.strptime('0110', "%d%m")
    },
    {
    "text" : "Когда перелётные птицы летят большими стаями – то это к дружной весне",
     "date_s" :  datetime.strptime('1003', "%d%m"),
     "date_e" :  datetime.strptime('0110', "%d%m")
    },
    {
    "text" : "Когда прилетели дрозды, то морозов уже не будет",
     "date_s" :  datetime.strptime('1003', "%d%m"),
     "date_e" :  datetime.strptime('0110', "%d%m")
    },
    {
    "text" : "Купаются воробьи ранней весной – к теплу",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('0110', "%d%m")
    },
    {
    "text" : "У человеческого жилья много синиц, значит, весна будет холодной",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Если в марте видно дятла, то весна поздней будет",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Ласточка вылетает – тёплый день обещает",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Ласточка низко летает – дождь обещает.",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Увидел скворца – знай: весна у порога",
     "date_s" :  datetime.strptime('2502', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Журавль прилетел – скоро лёд сойдёт",
     "date_s" :  datetime.strptime('0104', "%d%m"),
     "date_e" :  datetime.strptime('1504', "%d%m")
    },
    {
    "text" : "Когда снег растает с южной стороны муравейника – то лето будет холодным и коротким, а когда снег тает с северной стороны – тёплым и продолжительным",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : " Март сухой, апрель сырой, май холодный – год хлебородный",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3105', "%d%m")
    },
    {
    "text" : " Март холодный – год хлебородный",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Когда ранней весной сверкает молния, а грома не слышно – будет сухое лето",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3103', "%d%m")
    },
    {
    "text" : "Первый гром гремит при южном ветре – то и весна будет тёплой, при западном – дождливая, при северном – холодная, при восточном – тёплая и сухая",
     "date_s" :  datetime.strptime('0103', "%d%m"),
     "date_e" :  datetime.strptime('3105', "%d%m")
    },
    {
    "text" : "Если с крыш висят длинные сосульки, то и весна будет длинной",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Больше снега – больше хлеба",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Зима без снега, лето без хлеба",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "В начале зимы шел сильный снег, в начале лета пойдет сильный дождь.Если снег выпадает, когда лист с дерева не спадает, то зима будет лютой",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Гром зимой – к сильным морозам",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Днем был сильный мороз, а к вечеру потеплело – жди длительную стужу",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Если зимой вьюги – летом ненастье",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Если зимой сухо и холодно, то и летом будет сухо и жарко. Если зимой тепло – летом будет холодно",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Если зимою иней – летом роса",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Кошка на печи – к стуже, а кошка на полу – к теплу",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Сильно блестят зимою звезды – к морозу",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    },
    {
    "text" : "Снегирь под окном зимой чирикает – к оттепели",
     "date_s" :  datetime.strptime('0112', "%d%m"),
     "date_e" :  datetime.strptime('2802', "%d%m")
    }
    ]
    for i in a:
        sign = Signs(
                    text=i['text'],
                    date_s = i['date_s'],
                    date_e = i['date_e']
                    )
        sign.save()
    return 'saved'

@app.route('/map')
def map():
    template = env.get_template('map.html')
    return template.render()

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
    mesuremsent.save()

    return data_srt


if __name__ == '__main__':
    app.run(debug=True) #app.run()

# @app.route('/get_all_readings')
# def get_all_testimony():
#
#     readings = Mesurement.query.raw_output()
#     readings = readings.all()

# @app.route('/create')
# def create():
#     mesuremsent = Mesurement(temp=14, illumination=0.55, wind_speed=30, pressure=7)
#     mesuremsent.save()
#     return 'created'
#
# @app.route('/create_cloths')
# def create_cloths():
#     clothes = Clothes(name="Sandali", temp = 20, part_of_the_body = "Feet")
#     clothes.save()
#     return 'Сlothing created'

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
#     Date = Date.descending(Mesurement.date).limit(1).one()
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
