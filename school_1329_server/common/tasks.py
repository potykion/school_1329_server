import celery
import os
from django.core.mail import EmailMessage
from fcm_django.fcm import fcm_send_message

app = celery.Celery('school_1329_server')

app.conf.update(
    BROKER_URL=os.environ['REDIS_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDIS_URL']
)


@app.task()
def send_email(subject, body, to):
    if not isinstance(to, list):
        to = [to]

    email = EmailMessage(subject, body, to=to)
    return email.send()


@app.task()
def send_push(fcm_token, title, body):
    return fcm_send_message(fcm_token, title, body)
