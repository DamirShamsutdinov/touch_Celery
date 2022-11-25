# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.mail import send_mail

from birthday import settings
from birthday.celeryapp import app
from users.models import CustomUser
from users.service import send


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    current_date = datetime.now().date().strftime('%d-%m')
    for user in CustomUser.objects.all():
        if current_date == user.birthday.strftime('%d-%m'):
            send_mail(
                'Тема ДР'.decode('utf-8'),
                'С днем рождения братуха!, голова-2уха'.decode('utf-8'),
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
