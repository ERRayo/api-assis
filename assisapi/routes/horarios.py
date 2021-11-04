from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session
from assisapi.schemas.horarios import horario_esquema, horarios_esquema
from assisapi.model.dbassis import horarios, db

ruta_horarios = Blueprint('ruta-horarios', __name__)


###endponit - GET all horarios
@ruta_horarios.route('/horario', methods=['GET'])
def get_horarios():
    all_horarios = horarios.query.all()
    result = horarios_esquema.dump(all_horarios)
    return jsonify(result)

###endpoint - GET from ID horario
@ruta_horarios.route('/horario/<id>', methods=['GET'])
def get_alumno(id):
    horario_id = horarios.query.get(id)
    return horario_esquema.jsonify(horario_id)

###endpoint - POST Creacion de horario
@ruta_horarios.route('/horario', methods=['POST'])
def create_horario():
    lunes = request.json['lunes']
    martes = request.json['martes']
    miercoles = request.json['miercoles']
    jueves = request.json['jueves']
    viernes = request.json['viernes']
    sabado = request.json['sabado']
    
    new_horario = horarios(lunes, martes, miercoles, jueves, viernes, sabado)
    db.session.add(new_horario)
    db.session.commit()
    return horario_esquema.jsonify(new_horario)

###endpoint - PUT horario
@ruta_horarios.route('/horario/<id>', methods=['PUT'])
def update_horario(id):
    horario_update = horarios.query.get(id)
    lunes = request.json['lunes']
    martes = request.json['martes']
    miercoles = request.json['miercoles']
    jueves = request.json['jueves']
    viernes = request.json['viernes']
    sabado = request.json['sabado']
    horario_update.lunes = lunes
    horario_update.martes = martes
    horario_update.miercoles = miercoles
    horario_update.jueves = jueves
    horario_update.viernes = viernes
    horario_update.sabado = sabado
    db.session.commit()
    return horario_esquema.jsonify(horario_update)

###endpoint - DELETE horario
@ruta_horarios.route('/horario/<id>', methods=['DELETE'])
def delete_horario(id):
    horario_delete = horarios.query.get(id)
    db.session.delete(horario_delete)
    db.session.commit()
    return horario_esquema.jsonify(horario_delete)