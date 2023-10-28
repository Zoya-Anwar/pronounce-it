# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)

words = [
    {"id": 1, "word": "abondé", "phoneme": "§"},
    {"id": 2, "word": "abdication", "phoneme": "§"},
    {"id": 3, "word": "évoquions", "phoneme": "§"},
]

def _find_next_id():
    return max(word["id"] for word in words) + 1

@app.get("/api/word")
def get_word():
    return jsonify(words)

@app.post("/api/find")
def add_country():
    if request.is_json:
        word = request.get_json()
        word["id"] = _find_next_id()
        words.append(word)
        return word, 201
    return {"error": "Request must be JSON"}, 415