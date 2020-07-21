import logging

from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity)
from flask_restx import Resource

from rest.app import bcrypt, db
from utils.auth import get_auth
from utils.constants import HTTPCode
from utils.response import api_response
from .models import User
from .schema import UserSchema

logger = logging.getLogger(__name__)


class UserSignup(Resource):
    def __init__(self, *args, **kwargs):
        self.schema = UserSchema()
        super().__init__(*args, **kwargs)

    def post(self):
        if len(request.json['username']) == 0 and len(request.json['password']) == 0 and len(
                request.json['email']) == 0:
            return jsonify({'error': 'Every fields are required.'})
        username = request.json['username']
        password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
        check_user = User.query.filter_by(username=username).first()
        if not check_user:
            user = User(username=username, email=request.json['email'], password=password, data='')
            db.session.add(user)
            db.session.commit()
            logger.info('User created successfully')
            return api_response(data=self.schema.dump(user), code=HTTPCode.HTTP_200_STATUS_OK)
        else:
            return api_response(msg='Username is already in use.', code=HTTPCode.HTTP_400_BAD_REQUEST)


class Login(Resource):
    def post(self):
        # get_data=request.json['data']
        if len(request.json['username']) == 0 or len(request.json['password']) == 0:
            return jsonify({'error': 'Username or password can not be  null.'})
        user = User.query.filter_by(username=request.json['username']).first()
        password = request.json['password']
        if user:
            check_pass = bcrypt.check_password_hash(user.password, password)
        else:
            return api_response(msg='Username does not exist.', code=HTTPCode.HTTP_400_BAD_REQUEST)
        if user and check_pass:
            logger.info('User retrieved successfully')
            auth_response = get_auth(user_id=user.id, fresh=True)
            return api_response(data=auth_response, code=HTTPCode.HTTP_200_STATUS_OK)
        return api_response(msg='Invalid username or password.', code=HTTPCode.HTTP_400_BAD_REQUEST)


class Refresh(Resource):
    def post(self):
        current_user = get_jwt_identity()
        ret = {
            'access': create_access_token(identity=current_user)
        }
        return api_response(data=ret, code=HTTPCode.HTTP_200_STATUS_OK)
