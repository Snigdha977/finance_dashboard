from flask import Blueprint, jsonify
from db import get_db
from utils.auth import role_required

summary_bp = Blueprint('summary_bp', __name__)


@summary_bp.route('/summary', methods=['GET'])
@role_required(['admin', 'analyst'])
def summary():
    conn = get_db()

    income = conn.execute("SELECT SUM(amount) FROM records WHERE type='income'").fetchone()[0] or 0
    expense = conn.execute("SELECT SUM(amount) FROM records WHERE type='expense'").fetchone()[0] or 0

    categories = conn.execute('''SELECT category, SUM(amount) as total
                                 FROM records GROUP BY category''').fetchall()

    recent = conn.execute('''SELECT * FROM records ORDER BY date DESC LIMIT 5''').fetchall()

    monthly = conn.execute('''SELECT strftime('%Y-%m', date) as month, SUM(CASE WHEN type='income' THEN amount ELSE 0 END) as income, SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) as expense FROM records GROUP BY month ORDER BY month DESC LIMIT 12''').fetchall()

    weekly = conn.execute('''SELECT strftime('%Y-%W', date) as week, SUM(CASE WHEN type='income' THEN amount ELSE 0 END) as income, SUM(CASE WHEN type='expense' THEN amount ELSE 0 END) as expense FROM records GROUP BY week ORDER BY week DESC LIMIT 12''').fetchall()

    conn.close()

    return jsonify({
        'total_income': income,
        'total_expense': expense,
        'net_balance': income - expense,
        'category_breakdown': [dict(c) for c in categories],
        'recent_activity': [dict(r) for r in recent],
        'monthly_trends': [dict(m) for m in monthly],
        'weekly_trends': [dict(w) for w in weekly]
    })