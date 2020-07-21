from rest.app import ma
from .models import Tag


class TagSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        model = Tag


class TagListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'label', 'value', 'color')
