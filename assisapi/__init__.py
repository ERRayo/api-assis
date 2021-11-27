from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from assisapi.config.default import configConexion



application = app = Flask(__name__)

app.config.from_object(configConexion['conexionDB'])

db = SQLAlchemy(app)
ma = Marshmallow(app)

from assisapi.routes.carreras import ruta_carreras
from assisapi.routes.materias import ruta_materias
from assisapi.routes.alumnos import ruta_alumnos
from assisapi.routes.grupos import ruta_grupos
from assisapi.routes.profesores import ruta_profesores
from assisapi.routes.horarios import ruta_horarios
from assisapi.routes.periodos import ruta_periodos

app.register_blueprint(ruta_carreras)
app.register_blueprint(ruta_materias)
app.register_blueprint(ruta_alumnos)
app.register_blueprint(ruta_grupos)
app.register_blueprint(ruta_profesores)
app.register_blueprint(ruta_horarios)
app.register_blueprint(ruta_periodos)