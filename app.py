from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return '{"status": true}'

@app.route('/submit', methods=['POST'])
def submit():
    return request.data

if __name__ == '__main__':
    app.run(debug=True) #app.run()
