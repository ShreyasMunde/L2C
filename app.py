from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Store the last result in memory (for simplicity)
last_result = None

# @app.route('/upload', methods=['POST'])
# def handle_upload():
#     global last_result
#     file = request.files['file']

#     colab_url = "https://your-colab-url.ngrok.io/predict"
#     files = {'file': (file.filename, file.stream, file.content_type)}

#     try:
#         response = requests.post(colab_url, files=files)
#         data = response.json()
#         last_result = data  # store it temporarily
#         return jsonify({"message": "File uploaded and being processed."})
#     except Exception as e:
#         print("Error:", e)
#         return jsonify({"error": "Failed to connect to Colab"}), 500

@app.route('/result', methods=['GET'])
def get_result():
    if last_result:
        return jsonify(last_result)
    else:
        return jsonify({"result": "No result available yet."}), 404

