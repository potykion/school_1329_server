import os
from datetime import datetime

import celery
from django.conf import settings
from django.core.mail import EmailMessage
from fcm_django.fcm import fcm_send_message

app = celery.Celery('school_1329_server')

app.conf.update(
    BROKER_URL=os.getenv('REDIS_URL'),
    CELERY_RESULT_BACKEND=os.getenv('REDIS_URL'),
    CELERY_ALWAYS_EAGER=settings.DEBUG
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


@app.task()
def send_notifications(notification_pk):
    from school_1329_server.notifications.models import Notification

    notification = Notification.objects.get(pk=notification_pk)

    user_tokens = notification.fetch_target_users().values_list('fcm_token', flat=True)
    for token in user_tokens:
        send_push(token, 'Sch1329', notification.text)

    notification.sent = True
    notification.save()

    if not notification.send_once and not notification.deadline_came:
        notification.schedule()
