from flask import Flask
from controllers.arithmetic import arithmetic
from controllers.auth import auth

def router():
    app = Flask(__name__)
    app.register_blueprint(auth , url_prefix="/auth")
    app.register_blueprint(arithmetic ,url_prefix='/arithmetic')
    return app
