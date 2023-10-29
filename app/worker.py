from time import sleep
from celery import Celery

BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

celery_app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery_app.task
def celery_worker(a, b):
    sleep(60)  # Simula um atraso de 10 segundos
    return a + b  # Retorna o resultado após a simulação
