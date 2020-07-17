from datetime import timedelta

from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_refresh_token_required,
                                get_jwt_identity)
from flask_restful import Resource

from apps.functions.logger import get_logger
from rest.app import db
from .models import User
from .schema import user_schema

bcrypt = Bcrypt()
logger = get_logger()

user = Blueprint('user', __name__)


class Users(Resource):
    def post(self):
        if len(request.json['username']) == 0 and len(request.json['password']) == 0 and len(
                request.json['email']) == 0:
            return jsonify({'error': 'Every fields are required.'})
        username = request.json['username']
        password = bcrypt.generate_password_hash(request.json['password'])
        check_user = User.query.filter_by(username=username).first()
        if not check_user:
            check_email = User.query.filter_by(email=request.json['email']).first()
            if not check_email:
                create_user = User(username=username, email=request.json['email'], password=password, data='')
                db.session.add(create_user)
                db.session.commit()
                logger.info('User created successfully')
                return user_schema.jsonify(create_user)
            else:
                return jsonify({'error': 'Email is already in use.'})
        else:
            return jsonify({'error': 'Username is already in use.'})


class Login(Resource):
    def post(self):
        # get_data=request.json['data']
        if len(request.json['username']) == 0 or len(request.json['password']) == 0:
            return jsonify({'error': 'Username or password can not be  null.'})
        get_user = User.query.filter_by(username=request.json['username']).first()
        if get_user:
            check_pass = bcrypt.check_password_hash(get_user.password, request.json['password'])
        else:
            return jsonify({'error': 'Username does not exist.'})
        if get_user and check_pass:
            result = user_schema.dump(get_user)
            logger.info('User retrieved successfully')
            access_expires = timedelta(minutes=60)
            refresh_expires = timedelta(days=365)
            access_token = create_access_token(identity=get_user.username, expires_delta=access_expires, fresh=True)
            refresh_token = create_refresh_token(identity=get_user.username, expires_delta=refresh_expires)
            return jsonify(
                {'user': '{}'.format(get_user.username), 'access_token': access_token, 'refresh_token': refresh_token,
                 'data': get_user.data})
        return jsonify({'error': 'Invalid user or password'})


class Refresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        current_user = get_jwt_identity()
        access_expires = timedelta(minutes=60)
        new_token = create_access_token(identity=current_user, expires_delta=access_expires, fresh=False)
        ret = {'user': current_user, 'access_token': new_token}
        return jsonify(ret)
