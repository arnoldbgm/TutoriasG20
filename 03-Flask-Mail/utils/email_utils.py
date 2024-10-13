from flask_mail import Message
from flask import render_template


def send_welcome_email(to_email, username):
    from app import mail  # Importación tardía para evitar ciclos
    msg = Message('Bienvenido a nuestra aplicación', recipients=[to_email])
    msg.html = render_template('welcome_email.html', username=username)
    mail.send(msg)
