import os
from flask import Flask, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, static_folder=STATIC_DIR)
CORS(app)

@app.route('/')
def index():
    return send_from_directory(STATIC_DIR, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    target = os.path.join(STATIC_DIR, path)
    if os.path.exists(target) and not os.path.isdir(target):
        return send_from_directory(STATIC_DIR, path)
    return send_from_directory(STATIC_DIR, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[*] RUNNN server running at http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=False)