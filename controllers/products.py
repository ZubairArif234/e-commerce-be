from flask import Blueprint , jsonify,request,session
from config.database import db
from modals.product import Product
from decorators.isAuth import isAuth
from flask_jwt_extended import get_jwt_identity


product = Blueprint("product" , __name__)
myCollection = db['products']

@product.route('/create',methods=['POST'])
@isAuth
def createProduct ():
    # current_user = get_jwt_identity()
    # print(current_user)
    userDetail = session.get('user')
    print(userDetail)
    try:
        data = request.get_json()
        product = Product(
          name="Product Name",
          desc="Product Description",
          price="100",
          shades={"color": "red"},
          sizes={"S": 5, "M": 10}
)
        product.save()
        return jsonify({"message": "Product created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500