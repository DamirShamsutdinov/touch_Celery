# -*- coding: utf-8 -*-
from django.core.mail import send_mail

from birthday import settings


def send(user_email):
    send_mail(
        'Тема ДР'.decode('utf-8'),
        'Вы зареганы на рассылку поздравлений с Днем варения'.decode('utf-8'),
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
