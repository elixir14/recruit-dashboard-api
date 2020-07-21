import logging
import traceback

from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restx import Api
from jwt import ExpiredSignatureError

from utils.constants import HTTPCode
from utils.response import api_response

logger = logging.getLogger(__name__)

api = Api(
    version="1.0",
    title="Recruit Dashboard API",
)


@api.errorhandler(ExpiredSignatureError)
def handle_signature_expiration_exception(error):
    logger.exception(traceback.print_stack())
    return api_response(msg=error.__str__(), code=HTTPCode.HTTP_401_UNAUTHORIZED)


@api.errorhandler(NoAuthorizationError)
def handle_signature_expiration_exception(error):
    logger.exception(traceback.print_stack())
    return api_response(msg=error.__str__(), code=HTTPCode.HTTP_401_UNAUTHORIZED)
