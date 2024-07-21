from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(message=f"You said: {data['message']}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all network interfaces
