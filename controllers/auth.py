from flask import Blueprint , request ,jsonify
from flask_jwt_extended import JWTManager 
from modals.user import User
import bcrypt

jwt = JWTManager()

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['POST'])
def login ():
    data= request.get_json()
    

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    
    user = User(username=data['username'],email=data['email'],password=hashed_password)
    user.save()
    print(user)
    return jsonify({"message": "User created successfully"}), 201