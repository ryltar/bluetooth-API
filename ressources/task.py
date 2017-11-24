from celery import Celery
from celery.schedules import crontab
from pybluez import mainloop
import json
import os

app = Celery('inquiry')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, inquiry.s(), name="inquiry every 9")
   

@app.task
def inquiry():
    with open("./ressources/devices.json", 'w') as f:
        content = mainloop()
        json.dump(content,f)

def main():
    app.start(argv=['celery', 'worker', '-B'])
