from flask_restful import Resource
from pybluez import mainloop
from flask import jsonify
import json

class Bluetooth(Resource):
    def get(self):
        with open('./ressources/devices.json','r') as file:
            devices = file.read()
        try:
            return json.loads(devices)
        except:
            return json.loads(json.dumps(["worker are trying to reload device list"]))
