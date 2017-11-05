from flask import Flask
from flask_restful import Api
from ressources import Bluetooth

app = Flask(__name__)
api = Api(app)


api.add_resource(Bluetooth, '/');

if __name__ == '__main__':
    app.run(debug=True)