from dotenv import load_dotenv
from flask_cors import CORS
from router import router
from mongoengine import connect
from config.database import mongo_connection
import os

db = mongo_connection()
load_dotenv()
app = router()
CORS(app)
connect(db='advance_calculator',host=os.getenv('MONGO_URI'))
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_ENV')


if __name__ == "__main__":
    app.run(debug=True)