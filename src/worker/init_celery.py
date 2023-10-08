import os
from celery import Celery
from config import CELERY_CONFIG

celery = Celery(__name__, backend=CELERY_CONFIG.CELERY_RESULT_BACKEND, broker=CELERY_CONFIG.CELERY_BROKER_URL)
