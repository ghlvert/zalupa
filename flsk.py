from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>ZALUPA</h1>'

@app.route('info')
def info():
    return '<h1>info</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')