from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<H1>Hello Deventer</H1>'

app.run(host='0.0.0.0', port=80)