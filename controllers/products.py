from flask import Blueprint , jsonify,request,session
from config.database import db
from modals.product import Product
from decorators.isAuth import isAuth


product = Blueprint("product" , __name__)
myCollection = db['products']

@product.route('/create',methods=['POST'])
@isAuth
def createProduct ():
    # current_user = get_jwt_identity()
    # print(current_user)
    userDetail = session.get('user')
    print(userDetail)
    print(request.form)
    try:
        # data = request.get_json()
     
       
            
        product = Product(
        name = request.form.get('name'),
        desc =request.form.get('desc'),
        price = request.form.get('price'),
       shades = request.form.getlist('shades[]'),
        sizes = request.form.getlist('sizes[]')
            #  thumbnailImg = image
        )
        product.save()
        return jsonify({"message": "Product created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500