from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/sobre")
def sobre():
    return "<h1>Revenda de sisstemas para o seu estabelecimento</h1>"

@app.route("/contato")
def contato():
    return