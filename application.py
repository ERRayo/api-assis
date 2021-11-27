from assisapi import app
from assisapi.config.default import configApp

if __name__=="__main__":  
    app.config.from_object(configApp['development'])
    app.run()