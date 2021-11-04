from flask import Flask, request, jsonify, Blueprint 
from schemas.profesores import profesor, profesores_esquema, profesor_esquema, db

ruta_profesores = Blueprint('ruta-profesores', __name__)

###endponit - GET all profesores 
@ruta_profesores.route('/profesor', methods=['GET'])
def get_profesores():
    all_profesores = profesor.query.all()
    result = profesores_esquema.dump(all_profesores)
    return jsonify(result)

###endpoint - GET from ID profesor
@ruta_profesores.route('/profesor/<id>', methods=['GET'])
def get_profesor(id):
    profesor_id = profesor.query.get(id)
    return profesor_esquema.jsonify(profesor_id)

###endpoint - POST Creacion de profesor
@ruta_profesores.route('/profesor', methods=['POST'])
def create_profesor():
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    no_trabajador = request.json['no_trabajador']
    new_profesor = profesor(nombre, apellidos, no_trabajador)
    db.session.add(new_profesor)
    db.session.commit()
    return profesor_esquema.jsonify(new_profesor)

###endpoint - PUT profesor
@ruta_profesores.route('/profesor/<id>', methods=['PUT'])
def update_profesor(id):
    profesor_update = profesor.query.get(id)
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    no_trabajador= request.json['no_trabajador']
    profesor_update.nombre = nombre
    profesor_update.apellidos = apellidos
    profesor_update.no_trabajador = no_trabajador
    db.session.commit()
    return profesor_esquema.jsonify(profesor_update)

###endpoint - DELETE profesor
@ruta_profesores.route('/profesor/<id>', methods=['DELETE'])
def delete_profesor(id):
    profesor_delete = profesor.query.get(id)
    db.session.delete(profesor_delete)
    db.session.commit()
    return profesor_esquema.jsonify(profesor_delete)