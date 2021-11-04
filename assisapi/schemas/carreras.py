from flask import Flask
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion
from marshmallow import fields

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
ma = Marshmallow(app)

#Esquema de la tabla carreras
class CarrerasEsquema(ma.Schema):    
    class Meta:
        fields = ('id','nombre','plan_estudios')
        ordered = True

#instancia de una sola carrera
carrera_esquema = CarrerasEsquema()

#instancia de varias carreras
carreras_esquema = CarrerasEsquema(many=True)