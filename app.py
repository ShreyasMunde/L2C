from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp"
SAVED_FILE_PATH = os.path.join(UPLOAD_FOLDER, "uploaded_file.png")
last_result = None

@app.route('/upload', methods=['POST'])
def handle_upload():
    global last_result

    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    file.save(SAVED_FILE_PATH)
    last_result = {"status": "File saved", "filename": file.filename}

    return jsonify({"message": "File uploaded successfully."})

@app.route('/result', methods=['GET'])
def get_result():
    if last_result:
        return jsonify(last_result)
    else:
        return jsonify({"error": "No result available yet."}), 404

@app.route('/download', methods=['GET'])
def download_file():
    if os.path.exists(SAVED_FILE_PATH):
        return send_file(SAVED_FILE_PATH, mimetype='image/png')
    else:
        return jsonify({"error": "File not found"}), 404
