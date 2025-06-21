from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.ocr_utils import extract_text_from_file
from utils.summarize_utils import summarize_text
from utils.db_utils import save_summary, get_user_summaries
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) 
UPLOAD_FOLDER = 'temp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/summarize', methods=['POST'])
def summarize():
    
    file = request.files['file']
    username = request.form.get('username')
    print(f"🧾 Received file: {file.filename} from {username}")
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = extract_text_from_file(filepath)
    summary = summarize_text(text)

    save_summary(username, text, summary)
    os.remove(filepath)
    return jsonify({'summary': summary})

@app.route('/api/history/<username>', methods=['GET'])
def history(username):
    data = get_user_summaries(username)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)