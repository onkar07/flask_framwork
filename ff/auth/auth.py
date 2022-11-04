from crypt import methods
from unicodedata import name
from flask import request, Blueprint, jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token,set_refresh_cookies,
create_refresh_token,jwt_required,get_jwt_identity,set_access_cookies,get_jwt)
from werkzeug.exceptions import Conflict,BadRequest
from datetime import datetime, timedelta, timezone
from auth.controller import *


auth_bp = Blueprint('auth_bp',__name__, static_url_path='assets')


@auth_bp.route("/login", methods=['POST'])
def login():
    response = auth_login(request)
    print(request.get_json())
    if(response == "Invalid User"): return  jsonify(msg="Invalid user")
    return response, HTTPStatus.OK

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    response = auth_refresh_token(request)
    return response,HTTPStatus.OK


@auth_bp.route('/verify', methods=['GET'])
@jwt_required(locations=['headers'])
def verify():
    return jsonify({"msg":"loggedin"})
        
