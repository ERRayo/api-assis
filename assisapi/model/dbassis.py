from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from assisapi.config.default import configConexion

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
db = SQLAlchemy(app)

#definicion del model de la tabla carreras
class carreras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    plan_estudios = db.Column(db.String(45))

    def __init__(self,nombre,plan_estudios):
        self.nombre = nombre
        self.plan_estudios = plan_estudios