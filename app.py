import os
from flask import Flask, render_template, request
from email.message import EmailMessage
import smtplib
import email
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


csrf = CSRFProtect()

class form_email(FlaskForm):
    name = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio')])
    subject = StringField('Assunto', validators=[DataRequired('Assunto não pode ficar vazio')])
    message = TextAreaField('Mensagem', validators=[DataRequired('Mensagem não pode ficar vazio')])


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


def form():
    seu_nome = request.form.get('seu_nome')
    seu_email = request.form.get('seu_email')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')

    title = 'Fale conosco! '
    return render_template("index.html", title=title, seu_nome=seu_nome, seu_email=seu_email, assunto=assunto, mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)