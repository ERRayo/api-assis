from flask import Flask
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion
from marshmallow import fields

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
ma = Marshmallow(app)

#Esquema de la tabla grupos
class GruposEsquema(ma.Schema):     
    class Meta:  
        fields = ('id','id_profesor','id_materia','fecha_inicio','no_sesiones')

#instancia de un solo grupo
grupo_esquema = GruposEsquema()
#instancia de varios grupos
grupos_esquema = GruposEsquema(many=True)