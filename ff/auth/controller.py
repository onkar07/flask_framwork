from crypt import methods
from unicodedata import name
from flask import request, Blueprint, jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token,set_refresh_cookies,
create_refresh_token,jwt_required,get_jwt_identity,set_access_cookies,get_jwt,verify_jwt_in_request)
from werkzeug.exceptions import Conflict,BadRequest
from datetime import datetime, timedelta, timezone
from utils.sqlConnection import mysqlConnect

def auth_login(request):
    try:
        data=request.get_json()
        email=data.get('name')
        password=data.get('password')
        conn = mysqlConnect()
        sql = 'select * from user where name=%s and password=%s'
        cur = conn.cursor()
        val = [email,password]
        cur.execute(sql,val)
        output = cur.fetchall()
        user = output
        if(len(output) == 0): 
            return "Invalid User"
        print("user",user)
        userData = {"id":user[0][0],
                    "name":user[0][1],
                    "role":user[0][4]}
        conn.close()
        if (email == user[0][1]) and (password==user[0][3]):
            access_token=create_access_token(identity=userData)
            refresh_token=create_refresh_token(identity=userData)

            response = jsonify(
                acccess_token=access_token,
                refresh_token=refresh_token,
                is_success = True,
                userInfo = userData
            )
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response
        else:
            print("enter valid username and passwords")
            return "enter valid username and passwords"
    except Exception as e:
        print(e)
        return "loign failed"


def auth_refresh_token(request):
    exp_timestamp = get_jwt()["exp"]
    now = datetime.now(timezone.utc)
    target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
    if target_timestamp > exp_timestamp:
        user=get_jwt_identity()
        access_token=create_access_token(identity=user)
        response = jsonify({"msg": "login successful"})
        set_access_cookies(response, access_token)
    else: return jsonify({"msg": "not experied yet"})
    
    
    return {'access_token':access_token}

