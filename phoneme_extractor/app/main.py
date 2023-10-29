from fastapi import FastAPI
from starlette.requests import Request
from app.internal.phonetic_words import get_french_phonetic_words, get_english_phonetic_words

app = FastAPI()

# Define the API endpoint
@app.get("/api/find/french_phoneme/{ipa_letter}")
async def find_french_phoneme(ipa_letter: str, request: Request):
    french_word, french_phonetic_transcription = get_french_phonetic_words(ipa_letter)
    return {"french_word": french_word, "french_phonetic_transcription": french_phonetic_transcription}

# Define the API endpoint
@app.get("/api/find/english_phoneme/{ipa_letter}")
async def find_english_phoneme(ipa_letter: str, request: Request):
    english_word, english_phonetic_transcription = get_english_phonetic_words(ipa_letter)
    return {"english_word": english_word, "english_phonetic_transcription": english_phonetic_transcription}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
