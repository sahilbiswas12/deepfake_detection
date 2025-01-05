from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/start-process', methods=['GET'])
def start_process():
    try:
        return jsonify({"status": "success", "message": "Connection successful!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": "Connection unsuccessful!"}), 500

if __name__ == '__main__':
    app.run(debug=True)