import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message 
import smtplib

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    app.debug = True



@app.route('/contact', methods=['POST', 'GET'])
def contact(): 
    name = request.form.get('nome')
    email = request.form.get('email')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')


    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("welberthvieiratito@gmail.com", "************")
    server.sendmail("welberthvieiratito@gmail.com", email, assunto, name, mensagem,) 
    title = "Agradecemos o Contato!"
    return render_template("index.html", title=title, name=name, email=email, assunto=assunto, mensagem= mensagem)
    
