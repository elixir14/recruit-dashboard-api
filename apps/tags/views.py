import logging

from flask import request
from flask_restx import Resource
from marshmallow import ValidationError, EXCLUDE

from rest.app import db
from utils.constants import HTTPCode
from utils.response import api_response
from .models import Tag as TagModel
from .schema import TagSchema

logger = logging.getLogger(__name__)


class Tag(Resource):
    def __init__(self, *args, **kwargs):
        self.schema = TagSchema()
        super().__init__(*args, **kwargs)

    def put(self, id):
        get_tag = TagModel.query.get(id)
        if get_tag:
            name = request.json['name']
            color = request.json['color']
            get_tag.name = name
            get_tag.color = color
            logger.info('Tag updated successfully')
            return api_response(data=self.schema.dump(get_tag), code=HTTPCode.HTTP_200_STATUS_OK)
        else:
            return api_response(msg='Tag does not exist', code=HTTPCode.HTTP_400_BAD_REQUEST)

    def delete(self, id):
        get_tag = TagModel.query.get(id)
        if get_tag:
            db.session.delete(get_tag)
            db.session.commit()
            result = self.schema.dump(get_tag)
            logger.info('Tag deleted successfully')
            return api_response(data=result, code=HTTPCode.HTTP_200_STATUS_OK)
        else:
            return api_response(msg='Tag does not exist', code=HTTPCode.HTTP_400_BAD_REQUEST)


class TagList(Resource):
    def __init__(self, *args, **kwargs):
        self.schema = TagSchema()
        super().__init__(*args, **kwargs)

    def get(self):
        get_tag = TagModel.query.all()
        result = self.schema.dump(get_tag, many=True)
        logger.info('Tag retrieved successfully')
        return api_response(data=result, code=HTTPCode.HTTP_200_STATUS_OK)

    def post(self):
        request_data = request.json
        try:
            records = TagSchema(many=True).load(request_data, unknown=EXCLUDE)
        except ValidationError as ex:
            logger.exception(ex.messages)
            return api_response(data=ex.messages, code=HTTPCode.HTTP_400_BAD_REQUEST)
        db.session.add_all(records)
        db.session.commit()
        logger.info('Tags created successfully')
        return api_response(data=self.schema.dump(records, many=True), code=HTTPCode.HTTP_200_STATUS_OK)
