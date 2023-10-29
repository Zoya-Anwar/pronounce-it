from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request
import base64
from app.internal.audio.rate_pronounciation import phoneme_similarity
from app.internal.phonetic_words import get_french_phonetic_words, get_english_phonetic_words
from app.database.db import get_top_10_lowest_phoneme, get_user_level_value
from app.internal.generate_sentences import generate_sentence_french
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

username="John"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HEADERS = {"Access-Control-Allow-Origin": "*", "Content-Language": "en-US", "Content-Type": "application/json"}

username = "Eva"

# Define the API endpoint
@app.get("/api/find/french_phoneme/{ipa_letter}")
async def find_french_phoneme(ipa_letter: str, request: Request):
    french_word, french_phonetic_transcription = get_french_phonetic_words(ipa_letter)
    content = {"french_word": french_word, "french_phonetic_transcription": french_phonetic_transcription}
    return JSONResponse(content=content, headers=HEADERS)

# Define the API endpoint
@app.get("/api/find/english_phoneme/{ipa_letter}")
async def find_english_phoneme(ipa_letter: str, request: Request):
    english_word, english_phonetic_transcription = get_english_phonetic_words(ipa_letter)
    return {"english_word": english_word, "english_phonetic_transcription": english_phonetic_transcription}, 200

@app.get("/api/get_word")
async def get_new_word(request: Request):
    threshold = get_user_level_value(username)
    worst_phonemes = list(filter(lambda x: x["score"] < threshold, get_top_10_lowest_phoneme(username)))
    word = get_french_phonetic_words(random.choice(worst_phonemes)['phoneme'])[0]
    content = {"word": word}
    return JSONResponse(content=content, headers=HEADERS)

@app.get("/api/get_sentence")
async def get_new_sentence(request: Request):
    threshold = get_user_level_value(username)
    worst_phonemes = list(filter(lambda x: x["score"] < threshold, get_top_10_lowest_phoneme(username)))
    word = get_french_phonetic_words(random.choice(worst_phonemes)['phoneme'])[0]
    sentence = generate_sentence_french(word)
    content = {"word": sentence}
    return JSONResponse(content=content, headers=HEADERS)


@app.post("/api/level")
async def set_level(request: Request):
    json = await request.json()
    level = json["level"]
    # set_level if time
    return JSONResponse(content={}, headers=HEADERS)

@app.post("/api/audio")
async def check_audio(request: Request):
    json = await request.json()
    b64 = ["audiob64"]
    wav = base64.decodebytes(b64)
    with open("./internal/output.wav", "rb") as file:
        file.write(wav)
    # Perform test and then save to db
    content = {}
    return JSONResponse(content=content, headers=HEADERS)

@app.get("/api/find/similarities/{french_word}")
async def phoneme_similarities(french_word: str, request: Request):
    return phoneme_similarity(french_word), 200

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
