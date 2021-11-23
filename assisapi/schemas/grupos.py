from assisapi import ma
from marshmallow import fields

#Esquema de la tabla grupos
class GruposEsquema(ma.Schema):     
    class Meta:  
        fields = ('id','id_profesor','id_materia','no_sesiones','id_periodo')

#instancia de un solo grupo
grupo_esquema = GruposEsquema()
#instancia de varios grupos
grupos_esquema = GruposEsquema(many=True)