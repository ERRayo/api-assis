from flask import Flask
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion
from marshmallow import fields

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
ma = Marshmallow(app)

#Esquema de la tabla profesores
class ProfesoresEsquema(ma.Schema):     
    class Meta:  
        fields = ('id','nombre','apellidos','no_trabajador')

#instancia de un solo profesor
profesor_esquema = ProfesoresEsquema()
#instancia de varios profesores
profesores_esquema = ProfesoresEsquema(many=True)