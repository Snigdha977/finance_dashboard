from flask import Blueprint, request, jsonify
from db import get_db
from utils.auth import role_required
from utils.validators import validate_record
from datetime import datetime

record_bp = Blueprint('record_bp', __name__)


@record_bp.route('/records', methods=['POST'])
@role_required(['admin'])
def create_record():
    data = request.json
    if not validate_record(data):
        return jsonify({'error': 'Missing fields'}), 400

    conn = get_db()
    conn.execute('''INSERT INTO records (amount, type, category, date, notes)
                    VALUES (?, ?, ?, ?, ?)''',
                 (data['amount'], data['type'], data['category'],
                  data.get('date', datetime.now().strftime('%Y-%m-%d')),
                  data.get('notes', '')))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Record created'})

@record_bp.route('/records', methods=['GET'])
@role_required(['admin', 'analyst', 'viewer'])
def get_records():
    filters = request.args

    query = 'SELECT * FROM records WHERE 1=1'
    params = []

    if 'type' in filters:
        query += ' AND type=?'
        params.append(filters['type'])

    if 'category' in filters:
        query += ' AND category=?'
        params.append(filters['category'])

    if 'date' in filters:
        query += ' AND date=?'
        params.append(filters['date'])

    conn = get_db()
    records = conn.execute(query, params).fetchall()
    conn.close()

    return jsonify([dict(r) for r in records])
@record_bp.route('/records/<int:id>', methods=['PUT'])
@role_required(['admin'])
def update_record(id):
    data = request.json
    conn = get_db()

    conn.execute('''UPDATE records SET amount=?, type=?, category=?, date=?, notes=? WHERE id=?''',
                 (data['amount'], data['type'], data['category'],
                  data['date'], data['notes'], id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Record updated'})


@record_bp.route('/records/<int:id>', methods=['DELETE'])
@role_required(['admin'])
def delete_record(id):
    conn = get_db()
    conn.execute('DELETE FROM records WHERE id=?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Record deleted'})