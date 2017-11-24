from flask import Flask
from flask_restful import Api
from ressources import Bluetooth,task
import threading

app = Flask(__name__)
api = Api(app)


api.add_resource(Bluetooth, '/');

def first_func():
    app.run()

def second_func():
    task.main()

if __name__ == '__main__':
    first_thread = threading.Thread(target=first_func)
    second_thread = threading.Thread(target=second_func)
    first_thread.start()
    second_thread.start()
