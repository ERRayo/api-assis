from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion



app = Flask(__name__)

app.config.from_object(configConexion['conexionDB'])

db = SQLAlchemy(app)
ma = Marshmallow(app)

