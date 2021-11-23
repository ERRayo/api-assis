from assisapi import ma
from marshmallow import fields

#Esquema de la tabla alumnos
class AlumnosEsquema(ma.Schema):     
    id = fields.Integer()
    id_carrera = fields.Integer()
    nombre = fields.String()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    no_control = fields.String()
    activo = fields.Boolean()
    carrera = fields.Nested("CarrerasEsquema")


#instancia de un solo alumno
alumno_esquema = AlumnosEsquema()
#instancia de varios alumnos
alumnos_esquema = AlumnosEsquema(many=True)