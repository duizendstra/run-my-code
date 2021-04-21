from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_deventer():
    return "<H1>Hello Deventer</H1>"