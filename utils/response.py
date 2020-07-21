import json
import logging
from datetime import datetime, date, time
from uuid import UUID

from utils.constants import HTTPCode

logger = logging.getLogger(__name__)


def to_serializable(val):
    """JSON serializer for objects not serializable by default"""

    if isinstance(val, (datetime, date, time)):
        return val.isoformat()
    elif isinstance(val, UUID):
        return val.hex
    elif hasattr(val, '__dict__'):
        return val.__dict__
    return val


def api_response(msg="", code=None, data=None):
    if not code:
        code = HTTPCode.HTTP_500_INTERNAL_SERVER_ERROR
    if code not in [HTTPCode.HTTP_200_STATUS_OK, HTTPCode.HTTP_201_RESOURCE_CREATED]:
        logger.error(msg)
    is_json = isinstance(data, dict) or isinstance(data, list)
    if data:
        response = data if is_json else json.dumps(data, default=to_serializable)
    else:
        response = {'message': msg}
    return response, code
