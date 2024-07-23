from flask import Blueprint , request,jsonify
import numpy as np
from helper.index import convert_to_python_type

arithmetic = Blueprint("arithmetic",__name__)

# add api
@arithmetic.route('/add',methods=['Post'])
def add():
    data = request.get_json()
    result = np.add(data['x'],data['y'])
    result = convert_to_python_type(result)
    return jsonify(result=result)

# substract api
@arithmetic.route('/subtract',methods=['Post'])
def subtract():
    data = request.get_json()
    result = np.subtract(data['x'],data['y'])
    result = convert_to_python_type(result)
    return jsonify(result=result)

# multiply api
@arithmetic.route('/multiply',methods=['Post'])
def multiply():
    data = request.get_json()
    result = np.multiply(data['x'],data['y'])
    result = convert_to_python_type(result)
    return jsonify(result=result)

# divide api
@arithmetic.route('/divide',methods=['Post'])
def divide():
    data = request.get_json()
    result = np.divide(data['x'],data['y'])
    result = convert_to_python_type(result)
    return jsonify(result=result)