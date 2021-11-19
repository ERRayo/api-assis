from assisapi import ma
from marshmallow import fields

#Esquema de la tabla horarios
class HorariosEsquema(ma.Schema):
    class Meta:
        fields = ('id','lunes','martes','miercoles','jueves','viernes', 'sabado')

#instancia de un solo horario
horario_esquema = HorariosEsquema()
#instancia de varios horarios
horarios_esquema = HorariosEsquema(many=True)