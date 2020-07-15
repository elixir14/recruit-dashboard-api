import json
from datetime import datetime


def date_converter(o):
    if isinstance(o, datetime):
        return o.__str__()


def custom_response(msg="", code=500, data=None):
    if data:
        return json.dumps(data, default=date_converter), code
    return json.dumps(msg), code
