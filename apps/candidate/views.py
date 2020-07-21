import logging

from flask import Blueprint, request
from flask_restx import Resource
from marshmallow import ValidationError

from apps.tags.models import Tag
from rest.app import db
from utils.constants import HTTPCode
from utils.response import api_response
from .models import Candidate as CandidateModel
from .schema import CandidateSchema

logger = logging.getLogger(__name__)

candidate = Blueprint('candidate', __name__)


class Candidate(Resource):
    def __init__(self, *args, **kwargs):
        self.schema = CandidateSchema()
        super().__init__(*args, **kwargs)

    def put(self, id):
        candidate = CandidateModel.query.filter_by(uid=id).first()
        if candidate:
            try:
                update_candidate = self.schema.load(request.json)
            except ValidationError as ex:
                logger.exception(ex.messages)
                return api_response(code=HTTPCode.HTTP_400_BAD_REQUEST, msg=ex.__str__())
            candidate = update_candidate
            db.session.commit()
            logger.info('Record updated successfully')
            return api_response(code=HTTPCode.HTTP_200_STATUS_OK, data=self.schema.jsonify(candidate))
        else:
            return api_response(code=HTTPCode.HTTP_200_STATUS_OK, msg='Candidate Does not exist.')

    def delete(self, id):
        candidate = CandidateModel.query.get(id)
        if candidate:
            db.session.delete(candidate)
            db.session.commit()
            result = self.schema.dump(candidate)
            logger.info('Record deleted successfully')
            return api_response(code=HTTPCode.HTTP_200_STATUS_OK, data=result)
        else:
            return api_response(code=HTTPCode.HTTP_200_STATUS_OK, msg='Candidate Does not exist.')


class CandidateList(Resource):
    def __init__(self, *args, **kwargs):
        self.schema = CandidateSchema()
        super().__init__(*args, **kwargs)

    def get(self):
        candidates = CandidateModel.query.all()
        result = self.schema.dump(candidates, many=True)
        return api_response(data=result, code=HTTPCode.HTTP_200_STATUS_OK)


class CandidateTag(Resource):

    def post(self):
        tag_ids = request.json['tags']
        candidate_id = request.json['candidate_id']
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        candidate = CandidateModel.query.get(candidate_id)
        if not candidate:
            return api_response(msg='Candidate does not exist', code=HTTPCode.HTTP_200_STATUS_OK)
        candidate.addTags = tags
        db.session.commit()
        return api_response(msg='Tag added to candidate successfully', code=HTTPCode.HTTP_200_STATUS_OK)
