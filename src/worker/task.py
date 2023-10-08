from src.worker.init_celery import celery
from datetime import datetime
import pytz
from celery.schedules import crontab
from src.models.models import Birthday
from src.mail.mail import send_mail
from config import CELERY_CONFIG

celery.conf.enable_utc = CELERY_CONFIG.CELERY_ENABLE_UTC
celery.conf.timezone = CELERY_CONFIG.CELERY_TIME_ZONE

celery.conf.beat_schedule = {
    "birthday-task": {
        "task": "src.worker.task.birthdays_today",
        "schedule": crontab(hour=0, minute=5)
    }
}

def generate_bioler():
    boiler = 'Hello there\nHere\'s your birthday reminder report:\n'
    return boiler

@celery.task
def birthdays_today():
    to_send = False

    time = datetime.now(pytz.timezone(CELERY_CONFIG.CELERY_TIME_ZONE))
    todays_day = time.day
    todays_month = time.month
    mail_body = generate_bioler()

    query = Birthday.query.filter(Birthday.bday_month == todays_month).all()
    for bday in query:
        # print(dir(bday))
        if bday.bday_day == todays_day:
            mail_body += 'Today: {}\n'.format(bday.name)
            to_send = True
        if bday.bday_day == todays_day + 1:
            mail_body += 'Tomorrow: {}\n'.format(bday.name)
            to_send = True

    if(to_send):
        send_mail(mail_body)
    else:
        print('No Birthdays to send')

