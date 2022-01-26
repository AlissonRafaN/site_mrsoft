import os
from flask import Flask, render_template, request
from email.message import EmailMessage
import smtplib


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")



@app.route('/contact', methods=['POST', 'GET'])
def contact(): 
    msg = EmailMessage()


    msg['Subject']=request.form.get('assunto')
    msg['From']='Contato Mr.Soft'
    msg['To']='welberthvieiratito@gmail.com'
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("welberthvieiratito@gmail.com", "")
    server.send_message(msg) 
    title = "Agradecemos o Contato!"
    server.quit() 
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)