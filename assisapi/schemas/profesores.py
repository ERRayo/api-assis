from assisapi import ma
from marshmallow import fields

#Esquema de la tabla profesores
class ProfesoresEsquema(ma.Schema):     
    class Meta:  
        fields = ('id','nombre','apellido_paterno','apellido_materno','no_trabajador')

#instancia de un solo profesor
profesor_esquema = ProfesoresEsquema()
#instancia de varios profesores
profesores_esquema = ProfesoresEsquema(many=True)