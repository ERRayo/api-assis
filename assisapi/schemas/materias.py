from assisapi import ma
from marshmallow import fields


#Esquema de la tabla materias
class MateriasEsquema(ma.Schema):      
    id = fields.Integer()
    nombre = fields.String()    
    id_carrera = fields.String()
    carrera = fields.Nested("CarrerasEsquema")

    

#instancia de una sola materia
materia_esquema = MateriasEsquema()
#instancia de varias materia
materias_esquema = MateriasEsquema(many=True)