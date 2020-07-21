from marshmallow import fields

from rest.app import ma
from .models import Candidate


class CandidateSchema(ma.SQLAlchemyAutoSchema):
    tags = fields.Method('get_tags')

    def get_tags(self, obj):
        tags = []
        for j in obj.addTags:
            tags.append({'label': j.label, 'color': j.color, 'id': j.id, 'value': j.value})
        return tags

    class Meta:
        model = Candidate
