from fastapi import FastAPI
from starlette.requests import Request
import base64
from app.internal.phonetic_words import get_french_phonetic_words, get_english_phonetic_words

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
async def get_new_word():
    #Get new word for user with a bad phoneme
    # Get bad phonemes, then get new word from randomly selected bad phoneme
    # return word
    return 200


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
        with open("./internal/output.wav", "rb") as file:
            file.write(wav)
        
        return "test", 200
    return {"error": "Something went wrong :("}, 415

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
