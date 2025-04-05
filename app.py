from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

# Store the last result in memory
last_result = None

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    file_content = file.read()
    encoded_image = base64.b64encode(file_content).decode('utf-8')

    return jsonify({'image_base64': encoded_image})


@app.route('/result', methods=['GET'])
def get_result():
    if last_result:
        return jsonify(last_result)
    else:
        return jsonify({"result": "No result available yet."}), 404

if __name__ == '__main__':
    app.run(debug=True)
