class DevelopmentConfig():
    DEBUG = True

     

class ConexionDBConfig():
    MySQL_HOST = 'localhost:3306'
    MySQL_USER = 'root'
    MySQL_PASSWORD = 'admin'
    MySQL_DB = 'asistencias'

    SECRET_KEY = 'Test'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost:3306/db_assis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    

configApp = {
    'development': DevelopmentConfig
}

configConexion = {
    'conexionDB': ConexionDBConfig
}