from flask_restful import Api
from flask_cors import CORS
from apps.candidate.views import candidate, Candidate, CandidateList, CandidateTag
from apps.tags.views import tag, ListTag, TagUpdate,CreateTag
from apps.users.views import user, Users, Refresh,Login
from rest.app import app

app.register_blueprint(candidate)
app.register_blueprint(tag)
app.register_blueprint(user)
api = Api(app)
CORS(app)

api.add_resource(Candidate,'/candidate/<int:id>')
api.add_resource(CandidateList,'/candidates')
api.add_resource(TagUpdate,'/tag/<int:id>')
api.add_resource(CreateTag,'/tag/create')
api.add_resource(ListTag,'/tags')
api.add_resource(Users,'/users')
api.add_resource(Login,'/login')
api.add_resource(Refresh,'/refresh')
api.add_resource(CandidateTag,'/candidate/tag')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)