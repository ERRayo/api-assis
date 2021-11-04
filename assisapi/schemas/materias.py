from flask import Flask
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion
from marshmallow import fields
from assisapi.schemas.carreras import CarrerasEsquema

app = Flask(__name__)

app.config.from_object(configConexion['conexionDB'])

ma = Marshmallow(app)

#Esquema de la tabla materias
class MateriasEsquema(ma.Schema):      
    class Meta: 
        fields = ('id','nombre', 'id_carrera', 'rcarrerra')
        ordered = True
    rcarrerra = fields.Nested(CarrerasEsquema, many = True)

    
    

#instancia de una sola materia
materia_esquema = MateriasEsquema()
#instancia de varias materia
materias_esquema = MateriasEsquema(many=True)