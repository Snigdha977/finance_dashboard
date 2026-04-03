from flask import Flask, jsonify
from db import init_db
from routes.user_routes import user_bp
from routes.record_routes import record_bp
from routes.summary_routes import summary_bp

app = Flask(__name__)

# root route for basic check
@app.route('/')
def home():
    return jsonify({
        "message": "Finance Dashboard API is running"
    })

# register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(record_bp)
app.register_blueprint(summary_bp)

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not Found'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
