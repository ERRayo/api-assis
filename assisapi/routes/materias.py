from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from assisapi.schemas.materias import materia_esquema, materias_esquema
from assisapi.model.dbassis import materias, db

ruta_materias = Blueprint('ruta-materias', __name__)

###endponit - GET all materias 
@ruta_materias.route('/materia', methods=['GET'])
def get_materias(): 
    all_materias = db.session.query(materias)
    print("\n---> Resultado consulta<----\n")
    print(all_materias)
    print("\n---> Resultado consulta<----\n")
    result = materias_esquema.dump(all_materias)
    print(result)
    return jsonify(result)

###endpoint - GET from ID materia
@ruta_materias.route('/materia/<id>', methods=['GET'])
def get_materia(id):
    materia_id = materias.query.get(id)
    return materia_esquema.jsonify(materia_id)

###endpoint - POST Creacion de materia
@ruta_materias.route('/materia', methods=['POST'])
def create_materia():
    id_carrera = request.json['id_carrera']
    nombre = request.json['nombre'] 
    new_materia = materias(id_carrera, nombre)
    db.session.add(new_materia)
    db.session.commit()
    return materia_esquema.jsonify(new_materia)

###endpoint - PUT materia
@ruta_materias.route('/materia/<id>', methods=['PUT'])
def update_meteria(id):
    materia_update = materias.query.get(id)
    id_carrera = request.json['id_carrera']
    nombre = request.json['nombre']
    materia_update.id_carrera = id_carrera
    materia_update.nombre = nombre  
    db.session.commit()
    return materia_esquema.jsonify(materia_update)

###endpoint - DELETE materia
@ruta_materias.route('/materia/<id>', methods=['DELETE'])
def delete_materia(id):
    materia_delete = materias.query.get(id)
    db.session.delete(materia_delete)
    db.session.commit()
    return materia_esquema.jsonify(materia_delete)