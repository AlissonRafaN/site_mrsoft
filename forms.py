from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = TextField("Nome")
    email = TextField("Email")
    subject = TextField("Assunto")
    message = TextAreaField("Mensagem")
    submit = SubmitField("Enviar")