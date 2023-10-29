# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import base64

# gives words in "word_to_transcribe", "phonetic_transcription" form
from phonetic_words import get_french_phonetic_words, get_english_phonetic_words
from phonemes_allosaurus import get_phonemes

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

words = [
    {"id": 1, "word": "abondé", "phoneme": "§"},
    {"id": 2, "word": "abdication", "phoneme": "§"},
    {"id": 3, "word": "évoquions", "phoneme": "§"},
]

def _find_next_id():
    return max(word["id"] for word in words) + 1

@app.get("/api/word")
def get_word():
    return jsonify(words), 200

@app.get("/api/find/english_phoneme/{ipa_letter}")
def find_english_phoneme(ipa_letter: str, request: Request):
    if request.is_json:
        english_word, english_phonetic_transcription = get_english_phonetic_words(ipa_letter)
        return english_word, 200
    return {"error": "Request must be JSON"}, 415

@app.get("/api/find/french_phoneme/{ipa_letter}")
def find_french_phoneme(ipa_letter: str, request: Request):
    if request.is_json:
        french_word, french_phonetic_transcription = get_french_phonetic_words(ipa_letter)
        return french_word, 200
    return {"error": "Request must be JSON"}, 415

@app.post("/api/level")
def set_level(request: Request):
    if request.is_json:
        level = request.json["level"]
        # set_level if time
        return 200
    return {"error": "Request must be JSON"}, 415

@app.post("/api/submit_audio")
def check_audio(request: Request):
    if request.is_json:
        b64 = request.json["audiob64"]
        wav = base64.decodebytes(b64)
        # submit wav file for checking
        return "test", 200
    return {"error": "Something went wrong :("}, 415
