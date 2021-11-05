from flask import Flask
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion
from marshmallow import fields
from assisapi.schemas.carreras import CarrerasEsquema

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
ma = Marshmallow(app)

#Esquema de la tabla alumnos
class AlumnosEsquema(ma.Schema):     
    class Meta:  
        fields = ('id','id_carrera','nombre','apellidos','no_control','activo')

#instancia de un solo alumno
alumno_esquema = AlumnosEsquema()
#instancia de varios alumnos
alumnos_esquema = AlumnosEsquema(many=True)