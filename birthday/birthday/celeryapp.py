import os

import celery
from celery import Celery
from celery.schedules import crontab

print celery.__file__

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday.settings')

app = Celery('birthday')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'users.tasks.send_beat_email',
        # 'schedule': crontab(minute='*/1'),
        'schedule': crontab(hour='*/24'),
    },
}
