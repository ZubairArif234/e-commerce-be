from flask import Flask
from controllers.arithmetic import arithmetic
from controllers.auth import auth
from controllers.products import product
import os

def router():
    app = Flask(__name__)
    app.secret_key = os.getenv('APP_SECRET_SESSION')
    app.register_blueprint(auth , url_prefix="/auth")
    app.register_blueprint(arithmetic ,url_prefix='/arithmetic')
    app.register_blueprint(product ,url_prefix='/product')
    return app
