from flask import Blueprint

from rest.routes.api_definition import api
from rest.routes.endpoints import ns_v1 as ns_v1


def _configure_namespaces(api):
    """
        Add more namespaces HERE
    """
    # data_namespace
    api.add_namespace(ns_v1)


def configure_api(flask_app):
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)

    _configure_namespaces(api)
    flask_app.register_blueprint(blueprint)
