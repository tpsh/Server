from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return '{"status": true}'

@app.route('/submit_get')
def submit_get():
    return json.dumps(request.args)

@app.route('/submit', methods=['POST'])
def submit():
    return request.data

if __name__ == '__main__':
    app.run(debug=True) #app.run()
