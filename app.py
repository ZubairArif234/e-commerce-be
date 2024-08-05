from dotenv import load_dotenv
from flask_cors import CORS
from router import router
from mongoengine import connect
from flask_jwt_extended import JWTManager 
from config.database import mongo_connection
import os
import datetime

db = mongo_connection()
load_dotenv()
app = router()
CORS(app)
jwt = JWTManager()
connect(db='advance_calculator',host=os.getenv('MONGO_URI'))
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = 'uploads/'
# app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])



jwt.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)