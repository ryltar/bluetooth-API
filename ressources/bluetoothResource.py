from flask_restful import Resource
from pybluez import mainloop
from flask import jsonify

class Bluetooth(Resource):
    def get(self):
        return jsonify(mainloop());
