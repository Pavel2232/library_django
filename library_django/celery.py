import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_django.settings')
app = Celery('library_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
