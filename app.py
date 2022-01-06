from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/sobre")
def sobre():
    return "<h1>Revenda de sistemas para o seu estabelecimento</h1>"


@app.route("/contato")
def contato():
    return ""


@app.route("/produtos")
def produtos():
    return ""