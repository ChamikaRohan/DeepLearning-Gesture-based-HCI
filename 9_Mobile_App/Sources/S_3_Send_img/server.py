from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/file', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        return jsonify(message='No file part in the request'), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(message='No selected file'), 400
    filename = secure_filename(file.filename)  # Use secure_filename to prevent filename attacks
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify(message='File uploaded successfully', filename=filename), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
