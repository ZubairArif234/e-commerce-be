from pymongo import MongoClient
import os

def mongo_connection():
    try:
        mongo_uri = os.getenv('MONGO_URI')
        client = MongoClient(mongo_uri)
        db = client['advance_calculator']
        print("connected successfully")
        return db
    except Exception as e:
        print(f"Error: {e}")
        return None


db = mongo_connection()