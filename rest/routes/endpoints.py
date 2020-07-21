from flask_jwt_extended import jwt_required, jwt_refresh_token_required

from apps.candidate import views as v_candidates
from apps.tags import views as v_tags
from apps.users import views as v_users
from rest.routes.api_definition import api

ns_v1 = api.namespace('api', description='Base definitions Scout and Cellar API swagger')


@ns_v1.route('/signup')
class UserSignUpV1(v_users.UserSignup):

    @jwt_required
    def post(self):
        return super().post()


@ns_v1.route('/login')
class LoginV1(v_users.Login):

    def post(self):
        return super().post()


@ns_v1.route('/refresh')
class RefreshV1(v_users.Refresh):

    @jwt_refresh_token_required
    def post(self):
        return super().post()


@ns_v1.route('/tags')
class TagListV1(v_tags.TagList):

    @jwt_required
    def post(self):
        return super().post()

    @jwt_required
    def get(self):
        return super().get()


@ns_v1.route('/tag/<int:id>')
class TagV1(v_tags.Tag):

    @jwt_required
    def put(self, id):
        return super().put(id)

    @jwt_required
    def delete(self, id):
        return super().delete(id)


@ns_v1.route('/candidates')
class CandidateListV1(v_candidates.CandidateList):

    @jwt_required
    def get(self):
        return super().get()


@ns_v1.route('/candidate/<int:id>')
class CandidateV1(v_candidates.Candidate):

    @jwt_required
    def put(self, id):
        return super().put(id)

    @jwt_required
    def delete(self, id):
        return super().delete(id)


@ns_v1.route('/candidate/tag')
class CandidateTagV1(v_candidates.CandidateTag):

    @jwt_required
    def post(self):
        return super().post()
