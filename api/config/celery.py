import os
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = [
    Queue(
        'queue1', 
        Exchange('tasks',type="direct",durable=True,), 
        routing_key='tasks',
        queue_arguments={'x-max-priority': 10}
    ),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1

# app.conf.task_routes = {
#     "appname.tasks.*":{"queue":"queuename"},
#     "appname.tasks.taskname":{"queue":"queuename"}
# }

app.autodiscover_tasks()