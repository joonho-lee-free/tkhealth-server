from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, storage
import base64
import os
import json
from io import StringIO

app = Flask(__name__)

# 환경변수에서 Firebase 키 불러오기
firebase_key = os.environ.get("FIREBASE_KEY_JSON")
cred = credentials.Certificate(json.loads(firebase_key))
firebase_admin.initialize_app(cred, {
    'storageBucket': 'tkhealth-v2.appspot.com'
})

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    filename = data['filename']
    base64_data = data['base64']
    file_bytes = base64.b64decode(base64_data)

    blob = storage.bucket().blob(f"recordings/{filename}")
    blob.upload_from_string(file_bytes, content_type=data['filetype'])

    return jsonify({"status": "✅ 업로드 성공", "url": blob.public_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)