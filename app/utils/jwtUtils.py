import jwt
import os
from datetime import datetime, timedelta
from functools import wraps
from flask import request
from ..utils.response import sendResponse

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "joeljustin")


def generate_jwt_token(user_id):
    payload = {
        "userId": user_id,
        "exp": datetime.utcnow() + timedelta(hours=2),  # Token expires in 2 hours
        "iat": datetime.utcnow()  # Issued at time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def validate_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload  # Return the decoded payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired!"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token!"}


def jwt_required(f):
    """
    A decorator to require JWT token for access.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return sendResponse(status="error", message="Token is missing!")

        token = token.split("Bearer ")[-1]
        
        validation = validate_jwt_token(token)
        if "error" in validation:
            return sendResponse(status="error", message=validation["error"])

        request.user = validation  # Attach the decoded payload to the request
        print("request.user::", request.user)
        return f(*args, **kwargs)
    return decorated_function
