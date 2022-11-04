from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from utils.policy import requires_access_level
from eInterview.questions.controller import *

questions_bp = Blueprint('questions_bp',__name__, static_url_path='assets')



@questions_bp.route("/list", methods=['GET'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','teacher','sudo'])
def lists():
    return jsonify(listQuestions(request))

@questions_bp.route("/list/one", methods=['GET'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['admin','teacher','sudo'])
def listOne():
    return jsonify(listOneById(request))

@questions_bp.route("/create", methods=['POST'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['sudo','teacher'])
def create():
    return createQuestions(request)


@questions_bp.route("/update", methods=['PATCH'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['sudo','teacher'])
def update():
    return updateQuestions(request)


@questions_bp.route("/delete", methods=['DELETE'])
@jwt_required(locations=['headers'])
@requires_access_level(access_level=['sudo','teacher'])
def delete():
    return deleteQuestions(request)