from flask import Flask
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion
from marshmallow import fields

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
ma = Marshmallow(app)

#Esquema de la tabla horarios
class HorariosEsquema(ma.Schema):
    class Meta:
        fields = ('id','lunes','martes','miercoles','jueves','viernes', 'sabado')



#instancia de un solo horario
horario_esquema = HorariosEsquema()
#instancia de varios horarios
horarios_esquema = HorariosEsquema(many=True)