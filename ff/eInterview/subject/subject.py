from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from utils.policy import requires_access_level
from eInterview.subject.controller import *
subject_bp = Blueprint('subject_bp',__name__, static_url_path='assets')



@subject_bp.route("/list", methods=['GET'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','student','sudo'])
def lists():
    return subjectList(request)

@subject_bp.route("/add", methods=['POST'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','sudo'])
def create():
    return createSub(request)

@subject_bp.route("/update", methods=['PATCH'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','sudo'])
def update():
    return updateSub(request)

@subject_bp.route("/delete", methods=['DELETE'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','sudo'])
def delete():
    return deleteSub(request)



@subject_bp.route("/getQuestions", methods=['GET'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','student','sudo'])
def getQuestion():
    return getQuestions(request)