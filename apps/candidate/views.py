from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError

from apps.functions.logger import get_logger
from apps.tags.models import Tag
from rest.app import db
from .models import Candidate as CandidateModel
from .schema import candidate_schema

logger = get_logger()

candidate = Blueprint('candidate', __name__)


class Candidate(Resource):
    @jwt_required
    def put(self, id):
        candidate = CandidateModel.query.filter_by(uid=id).first()
        if candidate:
            try:
                update_candidate = candidate_schema.load(request.json)
            except ValidationError as ex:
                logger.exception(ex.messages)
                return jsonify({'error': ex.messages})
            candidate = update_candidate
            db.session.commit()
            logger.info('Record updated successfully')
            return candidate_schema.jsonify(candidate)
        else:
            return jsonify({'error': 'Candidate Does not exist.'})

    def delete(self, id):
        candidate = CandidateModel.query.get(id)
        if candidate:
            db.session.delete(candidate)
            db.session.commit()
            result = candidate_schema.dump(candidate)
            logger.info('Record deleted successfully')
            return jsonify(result)
        else:
            return jsonify({'error': 'Candidate Does not exist.'})


class CandidateList(Resource):
    @jwt_required
    def get(self):
        tags = {}
        tag_list = []
        candidates = CandidateModel.query.all()
        # for i in candidates:
        #     uid = i.uid
        #     for j in i.addTags:
        #         tag_list.append({'label': j.label, 'color': j.color, 'id': j.id, 'value': j.value})
        #     tags[uid] = tag_list
        #     tag_list = []
        result = candidate_schema.dump(candidates, many=True)
        # for i in result:
        #     i['tags'] = tags[i['uid']]
        return result


class CandidateTag(Resource):
    @jwt_required
    def post(self):
        tag_ids = request.json['tags']
        candidate_id = request.json['candidate_id']
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        candidate = CandidateModel.query.get(candidate_id)
        if not candidate:
            return jsonify('Candidate does not exist'), 400
        candidate.addTags = tags
        db.session.commit()
        return {'msg': 'updated'}, 200
