from flask_jwt_extended import create_access_token, create_refresh_token


def get_auth(user_id, fresh=False):
    identity = {
        "user_id": user_id,
    }

    response = {
        'access': create_access_token(identity=identity, fresh=fresh),
        'refresh': create_refresh_token(identity=identity)
    }

    return response
