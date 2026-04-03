from flask import request, jsonify
from functools import wraps


def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            role = request.headers.get('role')
            if role not in allowed_roles:
                return jsonify({'error': 'Access denied'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator