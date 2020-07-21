from rest.app import ma
from .models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Fields to expose
        model = User
