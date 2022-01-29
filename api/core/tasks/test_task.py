import celery
from core.celery import app
from time import sleep
@app.task(bind=True)
def debug_task(self):
    sleep(3)
    print("123")

class TestTask(celery.Task):

    def run(self):
            sleep(10)
            print("123")


TestTask = app.register_task(TestTask())
