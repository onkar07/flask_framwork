from functools import wraps
from flask import jsonify
from flask_jwt_extended import (get_jwt_identity)

def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = get_jwt_identity()
            except Exception as e:
                print("error in deco",e)
            role = data['role']
            if role not in access_level:
                print("permission denied")
                return jsonify({"msg": "permission denied"})
            else:
                return f(*args, **kwargs)
        return decorated_function
    return decorator



   