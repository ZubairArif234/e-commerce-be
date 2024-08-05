import os
import jwt
import bcrypt
import random
from modals.user import User
from config.database import db
from flask_jwt_extended import create_access_token
from datetime import datetime , timedelta
from flask import Blueprint, request, jsonify,session



auth = Blueprint('auth', __name__)

myCollection = db["user"]

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        isUserExist = User.objects(email=data["email"]).first()
        if isUserExist:
            return jsonify({"message": "User already exists"}), 400
        
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            password=hashed_password
        )
        user.save()
        
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        
        data = request.get_json()
        if not data['email'] or not data['password']:
            return jsonify({'message': 'Email and password are required'}), 400
        
        user = User.objects(email=data['email']).first()
        
        if not user:
            return jsonify({"message": "User is not registered"}), 400
            
        if not user.emailVerified:
            return jsonify({"message": "User is not verified"}), 400
            
        
        if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({"message": "Password does not match"}), 400
        
        jwt_secret_key = os.getenv('JWT_SECRET_KEY')
        if not jwt_secret_key:
            raise ValueError("JWT_SECRET_KEY is not set in environment variables")

        jwt_token = create_access_token(identity={"email": user['email']})
        
        user.update(isActive=True)
        # print(user.id)
        session['user'] = user.userDetail()
        return jsonify({"message": "User logged in successfully", "token": jwt_token , "user":user.userDetail()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@auth.route('/email-otp', methods=['POST'])
def emailOtp():
    try:
        data = request.get_json()
        
        if not data.get('email'):
            return jsonify({"message": "Email is required"}), 400
        
        user = User.objects(email = data['email']).first()
        
        if not user :
            return jsonify({"message": "User not exist"}), 400
        
        otp = random.randint(100000,900000)
        otpExpiration = datetime.now() + timedelta(minutes=10)
        
        
        user.update(verificationOtp = otp , otpExpiration = otpExpiration)
        
        print(otp)
        return jsonify({"message": "Email verification OTP ", "otp": otp}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@auth.route('/verify-email', methods=['POST'])
def verifyEmail():
    try:
        data = request.get_json()
        
        if not data['email'] or not data["emailVerificationOpt"]:
            return jsonify({"message": "Email and verification OTP is required"}), 400
        
        user = User.objects(email = data['email']).first()
        
        if not user :
            return jsonify({"message": "User not exist"}), 400
        
        if user.verificationOtp != data['emailVerificationOpt']:
           return jsonify({"message": "Invalid OTP"}), 400

        if user.otpExpiration < datetime.now():
           return jsonify({"message": "OTP has expired. Please request a new one."}), 400
        
        user.update(emailVerified=True , otpExpiration= None , verificationOtp= None)
        
        return jsonify({"message": "Email verified", }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    