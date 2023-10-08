from src.mail.init_mail import mail
from flask_mail import Message
from config import MAIL_CONFIG

def send_mail(body):
    msg = Message("HBD notification", sender=MAIL_CONFIG.SENDER, recipients=[MAIL_CONFIG.RECIEVER])
    msg.body = body
    mail.send(msg)