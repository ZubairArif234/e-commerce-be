from  functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask import jsonify

def isAuth(f):
    @wraps(f)
    def decorator_function( *args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        return f(*args, **kwargs)
    return decorator_function