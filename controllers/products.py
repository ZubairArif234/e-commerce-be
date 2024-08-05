from flask import Blueprint , jsonify,request,session
from config.database import db
from modals.product import Product
from decorators.isAuth import isAuth
from werkzeug.utils import secure_filename

import os

product = Blueprint("product" , __name__)
myCollection = db['products']

@product.route('/create',methods=['POST'])
@isAuth
def createProduct ():
    # current_user = get_jwt_identity()
    # print(current_user)
    userDetail = session.get('user')
    print(userDetail)
    print(request.files)
    try:
        if 'image' not in request.files:
            return jsonify({"error": "Upload Image "}), 400
        
        file = request.files["image"]
        
        if file :
            filename = secure_filename(file.filename)
            filepath=os.path.join('uploads/' , filename)
            file.save(filepath)
            thumbnailImg=filepath
         
       
            
        product = Product(
        name = request.form.get('name'),
        desc =request.form.get('desc'),
        price = request.form.get('price'),
        shades = request.form.getlist('shades[]'),
        sizes = request.form.getlist('sizes[]'),
        thumbnailImg=thumbnailImg
        )
        product.save()
        return jsonify({"message": "Product created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500