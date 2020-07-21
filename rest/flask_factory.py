import logging
import traceback

from rest.app import create_app
from rest.router import configure_api
from utils.constants import HTTPCode
from utils.response import api_response

app = create_app()

logger = logging.getLogger(__name__)

settings = app.config

configure_api(app)


@app.errorhandler(Exception)
def handle_exception(error):
    logger.exception(traceback.print_stack())
    response = {
        "message": error.__str__()
    }
    if app.debug:
        response['traceback'] = traceback.format_exc()
    return api_response(data=response, code=HTTPCode.HTTP_500_INTERNAL_SERVER_ERROR)
