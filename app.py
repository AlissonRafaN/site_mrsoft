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


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = form_email()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)