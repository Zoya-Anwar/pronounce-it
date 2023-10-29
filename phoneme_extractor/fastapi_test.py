from fastapi import FastAPI
from starlette.requests import Request
import random
import nltk

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

# Define the get_french_phonetic_words function
def get_french_phonetic_words(desired_phoneme: str):
    # Make sure you've downloaded and extracted the Lexique dataset
    lexique_file = './Lexique382.tsv'

    # Read the dataset
    lexique_entries = [line.split("\t") for line in open(lexique_file, "r")]

    # Create a list to store entries with the desired phoneme
    entries_with_phoneme = []

    # Populate the list with entries matching the desired phoneme
    for entry in lexique_entries:
        word, phoneme = entry[0].lower(), entry[1]
        if desired_phoneme in phoneme:
            entries_with_phoneme.append((word, phoneme))

    # Check if there are matching entries
    if not entries_with_phoneme:
        print(f"No entries found with the phoneme {desired_phoneme}")
    else:
        # Select a random entry with the desired phoneme
        random_entry = random.choice(entries_with_phoneme)

        word_to_transcribe, phonetic_transcription = random_entry
        print(f"Random word with phoneme {desired_phoneme}: {word_to_transcribe}")
        print(f"Phonetic transcription: {phonetic_transcription}")

        return word_to_transcribe, phonetic_transcription


def get_english_phonetic_words(desired_phoneme: str):
    # Define the path to your custom pronunciation dictionary file
    custom_dict_file = "./CMU.in.IPA.txt"

    # Create a dictionary to store word-to-IPA mapping
    custom_ipa_dict = {}

    # Create a list to store words with the desired phoneme
    words_with_phoneme = []

    # Read the custom dictionary from the file and populate the custom_ipa_dict
    with open(custom_dict_file, "r") as file:
        for line in file:
            parts = line.split(",")
            if len(parts) == 2:
                word, ipa_pronunciation = parts[0].strip(), parts[1].strip()
                custom_ipa_dict[word] = ipa_pronunciation

    # Iterate through the custom dictionary to find words with the desired phoneme
    for word, ipa_pronunciation in custom_ipa_dict.items():
        if desired_phoneme in ipa_pronunciation:
            words_with_phoneme.append((word, ipa_pronunciation))

    # Check if there are matching entries
    if not words_with_phoneme:
        print(f"No entries found with the phoneme {desired_phoneme}")
    else:
        # Select a random entry with the desired phoneme
        random_entry = random.choice(words_with_phoneme)
        word_to_transcribe, phonetic_transcription = random_entry
        print(f"Random word with phoneme {desired_phoneme}: {word_to_transcribe}")
        print(f"Phonetic transcription: {phonetic_transcription}")

        return word_to_transcribe, phonetic_transcription



# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

