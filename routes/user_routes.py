from flask import Blueprint, request, jsonify
from db import get_db
from utils.auth import role_required
from utils.validators import validate_user

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'])
@role_required(['admin'])
def create_user():
    data = request.json
    if not validate_user(data):
        return jsonify({'error': 'Invalid input'}), 400

    conn = get_db()
    conn.execute('INSERT INTO users (name, role, status) VALUES (?, ?, ?)',
                 (data['name'], data['role'], 'active'))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User created'})


@user_bp.route('/users', methods=['GET'])
@role_required(['admin'])
def get_users():
    conn = get_db()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    return jsonify([dict(u) for u in users])
