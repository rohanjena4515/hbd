import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

host = os.getenv('SUPABASE_HOST')
database = os.getenv('SUPABASE_DB')
user = os.getenv('SUPABASE_USER')
port = os.getenv('SUPABASE_PORT')
passwd = os.getenv('SUPABASE_PASSWD')

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=passwd,url=host + ':' + port,db=database)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = DB_URL 
FLASK_DEBUG = True
FLASK_ENV = 'development'

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 587
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True

RECEIVER_MAIL = os.getenv('REC_MAIL_USERNAME')

class MailConfig(object):
    SENDER = MAIL_USERNAME
    RECIEVER = RECEIVER_MAIL

class CeleryConfig(object):
    CELERY_BROKER_URL = os.getenv('REDIS_URI')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URI')
    CELERY_TIME_ZONE = 'Asia/Kolkata'
    CELERY_ENABLE_UTC = False

CELERY_CONFIG = CeleryConfig
MAIL_CONFIG = MailConfig