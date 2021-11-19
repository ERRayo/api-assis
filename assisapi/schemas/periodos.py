from assisapi import ma
from marshmallow import fields

#Esquema de la tabla periodo
class PeriodoEsquema(ma.Schema):      
    id = fields.Integer()
    fecha_ini = fields.String()    
    fecha_fin = fields.String()
    

#instancia de una sola periodo
periodo_esquema = PeriodoEsquema()
#instancia de varias periodo
periodos_esquema = PeriodoEsquema(many=True)