from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session
from assisapi.schemas.grupos import grupo_esquema, grupos_esquema
from assisapi.model.dbassis import grupos, db

ruta_grupos = Blueprint('ruta-grupos', __name__)

###endponit - GET all grupos 
@ruta_grupos.route('/grupo', methods=['GET'])
def get_grupos():
    all_grupos = grupos.query.all()
    print("\n------>\n")
    print(all_grupos)
    print("\n-------\n")
    result = grupos_esquema.dump(all_grupos)
    return jsonify(result)

###endpoint - GET from ID grupo
@ruta_grupos.route('/grupo/<id>', methods=['GET'])
def get_grupo(id):
    grupo_id = grupos.query.get(id)
    return grupo_esquema.jsonify(grupo_id)

###endpoint - POST Creacion de grupo
@ruta_grupos.route('/grupo', methods=['POST'])
def create_grupo():
    id_profesor = request.json['id_profesor']
    id_materia = request.json['id_materia']
    fecha_inicio = request.json['fecha_inicio']
    no_sesiones = request.json['no_sesiones']    
    new_grupo = grupos(id_profesor, id_materia, fecha_inicio, no_sesiones)
    db.session.add(new_grupo)
    db.session.commit()
    return grupo_esquema.jsonify(new_grupo)

###endpoint - PUT grupo
@ruta_grupos.route('/grupo/<id>', methods=['PUT'])
def update_grupo(id):
    grupo_update = grupos.query.get(id)
    id_profesor = request.json['id_profesor']
    id_materia = request.json['id_materia']
    fecha_inicio = request.json['fecha_inicio']
    no_sesiones = request.json['no_sesiones']    

    grupo_update.id_profesor = id_profesor
    grupo_update.id_materia = id_materia
    grupo_update.fecha_inicio = fecha_inicio
    grupo_update.no_sesiones = no_sesiones
    db.session.commit()
    return grupo_esquema.jsonify(grupo_update)

###endpoint - DELETE grupo
@ruta_grupos.route('/grupo/<id>', methods=['DELETE'])
def delete_grupo(id):
    grupo_delete = grupos.query.get(id)
    db.session.delete(grupo_delete)
    db.session.commit()
    return grupo_esquema.jsonify(grupo_delete)