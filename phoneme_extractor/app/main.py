from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request
import base64
from app.internal.phonetic_words import get_french_phonetic_words, get_english_phonetic_words
from app.internal.rate_pronounciation import phoneme_similarity

from app.database.db import get_top_10_lowest_phoneme, get_user_level_value
import random
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
import librosa
import soundfile as sf
import wave

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
    # worst_phonemes = filter(lambda x: x["score"] < threshold ,get_top_10_lowest_phoneme(username))
    # return find_french_phoneme(random.choice(worst_phonemes), None)
    french_word, french_phonetic_transcription = get_french_phonetic_words("e")
    content = {"word": french_word}
    return JSONResponse(content=content, headers=HEADERS)


@app.post("/api/level")
async def set_level(request: Request):
    json = await request.json()
    level = json["level"]
    # set_level if time
    return JSONResponse(content={}, headers=HEADERS)


@app.post("/api/audio")
async def check_audio(request: Request):
    logging.debug(request)
    formData = await request.form()
    wav = formData["file"].file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + "/internal/output.wav", "wb") as aud:
        aud.write(wav.read())

    x, _ = librosa.load(dir_path + "/internal/output.wav", sr=16000)
    sf.write(dir_path + "/internal/output2.wav", x, 16000)

    # Perform test and then save to db
    word = formData["word"]
    result = phoneme_similarity(word, dir_path + "/internal/output2.wav")
    content = result
    
    # add to database under user John 


    print(content)


    return JSONResponse(content=content, headers=HEADERS)


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
