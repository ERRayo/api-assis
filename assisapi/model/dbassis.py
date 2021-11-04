from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from assisapi.config.default import configConexion

app = Flask(__name__)
app.config.from_object(configConexion['conexionDB'])
db = SQLAlchemy(app)

#definicion del model de la tabla carreras
class carreras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    plan_estudios = db.Column(db.String(45))

    def __init__(self,nombre,plan_estudios):
        self.nombre = nombre
        self.plan_estudios = plan_estudios

        
#definicion del model de la tabla profesores
class profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    apellidos = db.Column(db.String(45))
    no_trabajador = db.Column(db.String(45))

    def __init__(self,nombre,apellidos,no_trabajador):
        self.nombre = nombre
        self.apellidos = apellidos
        self.no_trabajador = no_trabajador

#definicion del model de la tabla grupos
class grupos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_profesor = db.Column(db.Integer)
    id_materia = db.Column(db.Integer)
    fecha_inicio = db.Column(db.Date)
    no_sesiones = db.Column(db.Integer)

    def __init__(self, id_profesor, id_materia, fecha_inicio, no_sesiones):
        self.id_profesor = id_profesor
        self.id_materia = id_materia
        self.fecha_inicio = fecha_inicio
        self.no_sesiones = no_sesiones

#definicion del model de la tabla horarios
class horarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lunes = db.Column(db.String(50))
    martes = db.Column(db.String(50))
    miercoles = db.Column(db.String(50))
    jueves = db.Column(db.String(50))
    viernes = db.Column(db.String(50))
    sabado = db.Column(db.String(50))

def __init__(self, lunes, martes, miercoles, jueves, viernes, sabado):
    self.lunes = lunes
    self.martes = martes
    self.miercoles = miercoles
    self.jueves = jueves
    self.viernes = viernes
    self.sabado = sabado

#definicion del model de la tabla materias
class materias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carreras.id'))
    nombre = db.Column(db.String(45))
    rcarrerra = db.relationship('carreras', backref="materias", lazy='dynamic')
    

    def __init__(self,id_carrera,nombre):
        self.id_carrera = id_carrera
        self.nombre = nombre

#definicion del model de la tabla alumnos
class alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_carrera = db.Column(db.Integer)
    nombre = db.Column(db.String(45))
    apellidos = db.Column(db.String(45))
    no_control = db.Column(db.String(45))
    activo = db.Column(db.Boolean)

    def __init__(self,id_carrera,nombre,apellidos,no_control,activo):
        self.id_carrera = id_carrera
        self.nombre = nombre
        self.apellidos = apellidos
        self.no_control = no_control
        self.activo = activo