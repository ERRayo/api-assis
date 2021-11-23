from assisapi import ma
from marshmallow import fields, Schema

#Esquema de la tabla carreras
class CarrerasEsquema(Schema):
    id = fields.Integer()
    nombre = fields.String()
    plan_estudios = fields.String()
    #materias = fields.List(fields.Nested("MateriasEsquema"))
    


#instancia de una sola carrera
carrera_esquema = CarrerasEsquema()
#instancia de varias carreras
carreras_esquema = CarrerasEsquema(many = True)