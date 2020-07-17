from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError, EXCLUDE

from apps.functions.logger import get_logger
from rest.app import db
from .models import Tag
from .schema import tag_schema, tag_listSchema, TagSchema

logger = get_logger()

tag = Blueprint('tag', __name__)


class TagUpdate(Resource):
    @jwt_required
    def put(self, id):
        get_tag = Tag.query.get(id)
        if get_tag:
            name = request.json['name']
            color = request.json['color']
            get_tag.name = name
            get_tag.color = color
            logger.info('Tag updated successfully')
            return tag_schema.dump(get_tag)
        else:
            return jsonify({'error': 'Tag does not exist'})

    @jwt_required
    def delete(self, id):
        get_tag = Tag.query.get(id)
        if get_tag:
            db.session.delete(get_tag)
            db.session.commit()
            result = tag_schema.dump(get_tag)
            logger.info('Tag deleted successfully')
            return result
        else:
            return jsonify({'error': 'Tag does not exist'})


class ListTag(Resource):
    @jwt_required
    def get(self):
        get_tag = Tag.query.all()
        result = tag_listSchema.dump(get_tag, many=True)
        logger.info('Tag retrieved successfully')
        return result


class CreateTag(Resource):
    @jwt_required
    def post(self):
        request_data = request.json
        try:
            records = TagSchema(many=True).load(request_data, unknown=EXCLUDE)
        except ValidationError as ex:
            logger.exception(ex.messages)
            return jsonify(ex.messages), 400
        db.session.add_all(records)
        db.session.commit()
        logger.info('Tags created successfully')
        return TagSchema(many=True).dump(records)
