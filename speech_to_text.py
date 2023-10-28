import speech_recognition as sr
import nltk
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the CMU Pronouncing Dictionary
nltk.download('cmudict')
nltk.download('punkt')
pronouncing_dict = cmudict.dict()

# Replace "your_audio_file.wav" with the path to your specific WAV file
audio_file = "output.wav"

# Recognize the speech from the provided WAV file
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)

# Recognize the speech using the Google Web Speech API
try:
    recognized_text = recognizer.recognize_google(audio, language="fr-FR")
except sr.UnknownValueError:
    recognized_text = ""
except sr.RequestError as e:
    recognized_text = ""
    print(f"Could not request results from Google Speech Recognition service; {e}")

# Tokenize the recognized text into words
user_words = word_tokenize(recognized_text)

print(recognized_text)

# Obtain the phonemes for each word
user_phonemes = [pronouncing_dict[word][0] if word in pronouncing_dict else [] for word in user_words]

# Get the reference phoneme transcription
reference_word = "regarder"  # Replace with the specific word you want to transcribe
reference_transcription = pronouncing_dict.get(reference_word, [[]])[0]

# Compare user's phonemes with reference phonemes
mismatches = [i for i, (u, r) in enumerate(zip(user_phonemes, reference_transcription)) if u != r]

# Calculate the pronunciation score
pronunciation_score = 1 - (len(mismatches) / len(reference_transcription))

print("Recognized Text:", recognized_text)
print(f"Pronunciation Score: {pronunciation_score}")
print(f"Mismatches: {[user_phonemes[i] for i in mismatches]}")



