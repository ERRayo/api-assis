from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from assisapi.schemas.alumnos import alumno_esquema, alumnos_esquema
from assisapi.model.dbassis import alumnos, db

ruta_alumnos = Blueprint('ruta-alumnos', __name__)

###endponit - GET all alumnos 
@ruta_alumnos.route('/alumno', methods=['GET'])
def get_alumnos():
    all_alumnos = alumnos.query.all()
    result = alumnos_esquema.dump(all_alumnos)
    return jsonify(result)

###endpoint - GET from ID alumno
@ruta_alumnos.route('/alumno/<id>', methods=['GET'])
def get_alumno(id):
    alumno_id = alumnos.query.get(id)
    return alumno_esquema.jsonify(alumno_id)

###endpoint - POST Creacion de alumno
@ruta_alumnos.route('/alumno', methods=['POST'])
def create_alumno():
    id_carrera = request.json['id_carrera']
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    no_control = request.json['no_control']
    activo = request.json['activo']
    new_alumno = alumnos(id_carrera, nombre, apellidos, no_control, activo)
    db.session.add(new_alumno)
    db.session.commit()
    return alumno_esquema.jsonify(new_alumno)

###endpoint - PUT alumno
@ruta_alumnos.route('/alumno/<id>', methods=['PUT'])
def update_alumno(id):
    alumno_update = alumnos.query.get(id)
    id_carrera = request.json['id_carrera']
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    no_control = request.json['no_control']
    activo = request.json['activo']
    alumno_update.id_carrera = id_carrera
    alumno_update.nombre = nombre
    alumno_update.apellidos = apellidos
    alumno_update.no_control = no_control
    alumno_update.activo = activo
    db.session.commit()
    return alumno_esquema.jsonify(alumno_update)

###endpoint - DELETE alumno
@ruta_alumnos.route('/alumno/<id>', methods=['DELETE'])
def delete_alumno(id):
    alumno_delete = alumnos.query.get(id)
    db.session.delete(alumno_delete)
    db.session.commit()
    return alumno_esquema.jsonify(alumno_delete)