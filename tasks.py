from celery import Celery

celery_app = Celery('tasks', broker='pyamqp://localhost//')


@celery_app.task()
def add_two_num(x, y):
    return x + y
