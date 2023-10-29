from fastapi import FastAPI
from starlette.requests import Request
import base64
from app.internal.phonetic_words import get_french_phonetic_words, get_english_phonetic_words
from app.internal.audio.rate_pronounciation import phoneme_similarity
from app.database.db import get_top_10_lowest_phoneme, get_user_level_value
from app.generate_sentences.py import generate_sentence_french
import random

app = FastAPI()

# Define the API endpoint
@app.get("/api/find/french_phoneme/{ipa_letter}")
async def find_french_phoneme(ipa_letter: str, request: Request):
    french_word, french_phonetic_transcription = get_french_phonetic_words(ipa_letter)
    return {"french_word": french_word, "french_phonetic_transcription": french_phonetic_transcription}, 200

# Define the API endpoint
@app.get("/api/find/english_phoneme/{ipa_letter}")
async def find_english_phoneme(ipa_letter: str, request: Request):
    english_word, english_phonetic_transcription = get_english_phonetic_words(ipa_letter)
    return {"english_word": english_word, "english_phonetic_transcription": english_phonetic_transcription}, 200

@app.get("/api/find/new_word")
async def get_new_word(request: Request):
    if request.is_json:
        username = request["username"]
        threshold = get_user_level_value(username)
        worst_phonemes = filter(lambda x: x["score"] < threshold, get_top_10_lowest_phoneme(username))
        return find_french_phoneme(random.choice(worst_phonemes), None)
    return {"error": "Meep noises"}, 415

@app.get("/api/find/new_sentence")
async def get_new_sentence(request: Request):
    if request.is_json:
        username = request["username"]
        threshold = get_user_level_value(username)
        worst_phonemes = filter(lambda x: x["score"] < threshold, get_top_10_lowest_phoneme(username))
        return generate_sentence_french(random.choice(worst_phonemes), None)
    return {"error": "Meep noises"}, 415


@app.post("/api/level")
async def set_level(request: Request):
    if request.is_json:
        level = request.json["level"]
        # set_level if time
        return 200
    return {"error": "Request must be JSON"}, 415

@app.post("/api/submit_audio")
async def check_audio(request: Request):
    if request.is_json:
        b64 = request.json["audiob64"]
        wav = base64.decodebytes(b64)
        with open("internal/audio/output.wav", "rb") as file:
            file.write(wav)
        # Perform test and then save to db
        return "test", 200
    return {"error": "Something went wrong :("}, 415

@app.get("/api/find/similarities/{french_word}")
async def phoneme_similarities(french_word: str, request: Request):
    return phoneme_similarity(french_word), 200

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
