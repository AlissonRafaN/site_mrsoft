
from flask import Flask, redirect, render_template
from forms import ContactForm
from flask import request
import pandas as pd
from flask_mail import Message, Mail


app = Flask(__name__)

app.secret_key = 'secretKey'

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contatomrsoft@gmail.com'
app.config["MAIL_PASSWORD"] = 'contatomrsoftcontato'

mail.init_app(app)



@app.route("/")
def homepage():
    return render_template("index.html")


@app.route('/contato', methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
       msg = Message(form.subject.data, sender='contatomrsoft@gmail.com', recipients=['mrsoftsistemas@gmail.com'])
       msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
       mail.send(msg)
    return render_template('contact.html', form=form)
   
if __name__ == "__main__":
    app.run(debug=True)

