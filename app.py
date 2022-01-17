from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre")

if __name__ == "__main__":
    app.run(debug=True)