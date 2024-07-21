from flask import Flask, request, jsonify
from MobileOperator import mobileoperator
from flask_cors import CORS

def create_server():
    app = Flask(__name__)
    CORS(app)

    @app.route('/action', methods=['POST'])
    def post_action():
        data = request.json
        if not data or 'data' not in data:
            return jsonify(message="Error: No data provided"), 400
        action = data['data']
        mobileoperator(action)
        return jsonify(message="Action data received successfully!")

    return app

def run_flask_server():
    app = create_server()
    app.run(host='0.0.0.0', port=8088)

if __name__ == '__main__':
    run_flask_server()
