from flask import Blueprint , request ,jsonify
from flask_jwt_extended import JWTManager 
from modals.user import User
from config.database import db
import bcrypt

jwt = JWTManager()

auth = Blueprint('auth',__name__)

myCollection = db["user"]

@auth.route('/login',methods=['POST'])
def login ():
    try:
        data= request.get_json()
        isUserExist = User.objects(email=data["email"]).first()
        if isUserExist :
            return jsonify({"message": "User already exist"}), 500
        print(isUserExist)

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(username=data['username'],email=data['email'],password=hashed_password)
       
    
        print(user)
        user.save()
        # myCollection.insert_one(user)
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 