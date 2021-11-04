from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from assisapi.schemas.carreras import carrera_esquema, carreras_esquema
from assisapi.model.dbassis import carreras, db

ruta_carreras = Blueprint('ruta-carreras', __name__)

###endponit - GET all carreras 
@ruta_carreras.route('/carrera', methods=['GET'])
def get_carreras():
    all_carreras = db.session.query(carreras)
    print(all_carreras)
    result = carreras_esquema.dump(all_carreras)
    return jsonify(result)

###endpoint - GET from ID carrera
@ruta_carreras.route('/carrera/<id>', methods=['GET'])
def get_carrera(id):
    carrera_id = carreras.query.get(id)
    return carrera_esquema.jsonify(carrera_id)

###endpoint - POST Creacion de carrera
@ruta_carreras.route('/carrera', methods=['POST'])
def create_carrera():
    nombre = request.json['nombre']
    plan_estudios = request.json['plan_estudios']
    new_carrera = carreras(nombre, plan_estudios)
    db.session.add(new_carrera)
    db.session.commit()
    return carrera_esquema.jsonify(new_carrera)

###endpoint - PUT carrera
@ruta_carreras.route('/carrera/<id>', methods=['PUT'])
def update_carrera(id):
    carrera_update = carreras.query.get(id)
    nombre = request.json['nombre']
    plan_estudios = request.json['plan_estudios']
    carrera_update.nombre = nombre
    carrera_update.plan_estudios = plan_estudios
    db.session.commit()
    return carrera_esquema.jsonify(carrera_update)

###endpoint - DELETE carrera
@ruta_carreras.route('/carrera/<id>', methods=['DELETE'])
def delete_carrera(id):
    carrera_delete = carreras.query.get(id)
    db.session.delete(carrera_delete)
    db.session.commit()
    return carrera_esquema.jsonify(carrera_delete)