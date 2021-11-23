from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from assisapi.schemas.periodos import periodo_esquema, periodos_esquema
from assisapi.model.dbassis import periodo, db
from assisapi import app

ruta_periodos = Blueprint('ruta-periodos', __name__)

###endponit - GET all periodo 
@ruta_periodos.route('/periodo', methods=['GET'])
def get_peridos():
    all_periodos = periodo.query.all()
    result = periodos_esquema.dump(all_periodos)
    return jsonify(result)

###endpoint - GET from ID periodo
@ruta_periodos.route('/periodo/<id>', methods=['GET'])
def get_periodo(id):
    periodo_id = periodo.query.get(id)
    return periodo_esquema.jsonify(periodo_id)

###endpoint - POST Creacion de periodo
@ruta_periodos.route('/periodo', methods=['POST'])
def create_periodo():
    fecha_ini = request.json['fecha_ini']
    fecha_fin = request.json['fecha_fin']
    
    new_periodo = periodo(fecha_ini, fecha_fin)

    db.session.add(new_periodo)
    db.session.commit()
    result = periodo_esquema.dump(new_periodo)
    return jsonify(result)

###endpoint - PUT periodo
@ruta_periodos.route('/periodo/<id>', methods=['PUT'])
def update_periodo(id):
    periodo_update = periodo.query.get(id)
    fecha_ini = request.json['fecha_ini']
    fecha_fin = request.json['fecha_fin']
    
    periodo_update.fecha_ini = fecha_ini
    periodo_update.fecha_fin = fecha_fin
    db.session.commit()
    return periodo_esquema.jsonify(periodo_update)

###endpoint - DELETE periodo
@ruta_periodos.route('/periodo/<id>', methods=['DELETE'])
def delete_periodo(id):
    periodo_delete = periodo.query.get(id)
    db.session.delete(periodo_delete)
    db.session.commit()
    return periodo_esquema.jsonify(periodo_delete)