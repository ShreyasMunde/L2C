from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if 'file' not in request.files:
            print("No file part in the request")
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        print(f"Received file: {file.filename}")

        colab_url = "https://your-ngrok-url.ngrok.io/predict"  # Update this with your live ngrok URL

        files = {'file': (file.filename, file.stream, file.content_type)}
        response = requests.post(colab_url, files=files)

        print(f"Colab response: {response.status_code}")
        return jsonify(response.json())

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500

