from assisapi import db

#definicion del model de la tabla carreras
class carrera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    plan_estudios = db.Column(db.String(45))
    rmaterias = db.relationship('materia', backref=db.backref('carrera', lazy=True))
    ralumno = db.relationship('alumno', backref=db.backref('carrera', lazy=True))

    def __init__(self,nombre,plan_estudios):
        self.nombre = nombre
        self.plan_estudios = plan_estudios
     
#definicion del model de la tabla profesores
class profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    apellido_paterno = db.Column(db.String(45))
    apellido_materno = db.Column(db.String(45))
    no_trabajador = db.Column(db.String(45))

    def __init__(self,nombre,apellido_paterno, apellido_materno,no_trabajador):
        self.nombre = nombre
        self.apellidos = apellidos
        self.no_trabajador = no_trabajador

#definicion del model de la tabla grupos
class grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_profesor = db.Column(db.Integer)
    id_materia = db.Column(db.Integer)
    no_sesiones = db.Column(db.Integer)
    id_periodo = db.Column(db.Integer)

    def __init__(self, id_profesor, id_materia, no_sesiones, id_periodo):
        self.id_profesor = id_profesor
        self.id_materia = id_materia
        self.no_sesiones = no_sesiones
        self.id_periodo = id_periodo

#definicion del model de la tabla horarios
class horario(db.Model):
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
class materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    nombre = db.Column(db.String(45))  
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id'))
    

    def __init__(self,id_carrera,nombre):
        self.id_carrera = id_carrera
        self.nombre = nombre

#definicion del model de la tabla alumnos
class alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id'))
    nombre = db.Column(db.String(45))
    apellido_paterno = db.Column(db.String(45))
    apellido_materno = db.Column(db.String(45))
    no_control = db.Column(db.String(45))
    activo = db.Column(db.Boolean)

    def __init__(self,id_carrera,nombre,apellido_paterno,apellido_materno,no_control,activo):
        self.id_carrera = id_carrera
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.no_control = no_control
        self.activo = activo

#definicion del model de la tabla periodo
class periodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    fecha_ini = db.Column(db.String(45))  
    fecha_fin = db.Column(db.String(45))  
    
    def __init__(self,fecha_ini,fecha_fin):
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin