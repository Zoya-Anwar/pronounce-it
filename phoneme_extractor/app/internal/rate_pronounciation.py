import speech_recognition as sr
import nltk
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize
from phonemes_allosaurus import get_phonemes
import epitran
import string
from ipapy import UNICODE_TO_IPA

input_file = "output.wav"
target_sentence = "avons"
target_tokens = word_tokenize(target_sentence.lower())


def which_recognized_words():
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
    user_tokens = word_tokenize(recognized_text.lower())

    valid = (user_tokens == target_tokens)
    print(f"The user words recognized are {user_tokens}")
    print(f"The target words were {target_tokens}")
    print(f"Is this the same? {valid}")

    return valid


def get_phonemes_descriptors(phonemes):
    phoneme_objects = []
    for p in phonemes:
        phoneme_objects.append(UNICODE_TO_IPA[p])

    return phoneme_objects

def get_target_generated_phonemes():
    # get generated phonemes
    generated = get_phonemes(filename=input_file).replace(" ", "")
    phonemes = get_phonemes_descriptors(generated)
    print(generated)
    print(len(phonemes))

    # get target phonemes
    epi = epitran.Epitran('fra-Latn-p')
    target = epi.transliterate(target_sentence.translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))
    target_phonemes = get_phonemes_descriptors(target)
    print(target)
    print(len(target_phonemes))

    return phonemes, target_phonemes

def score_phoneme_similarity(p1, p2):
    # consonants it will either be right or wrong
    # vowels can vary and merge into each other more
    # we need to separate consonants and vowels and measure the difference between them
    score = 0
    if p1.is_consonant == p2.is_consonant:
        score = score + 1
        for j in range(1, len(p1.descriptors)):
            if j < len(p1.descriptors) and j < len(p2.descriptors):
                desc1 = p1.descriptors[j]
                desc2 = p2.descriptors[j]
                if desc1 == desc2:
                    score = score + 1
            else:
                break

    return score

def phoneme_similarity():
    phonemes, target_phonemes = get_target_generated_phonemes()

    scores = []
    gen_i = 0
    tar_i = 0

    while tar_i < len(target_phonemes):
        target_phoneme = target_phonemes[tar_i]

        if len(phonemes) < gen_i:  # this is the case where more targets than generated
            scores.append((target_phoneme, 0))
            tar_i += 1
            continue

        original_score = score_phoneme_similarity(phonemes[gen_i], target_phoneme)

        if original_score >= 3:  # This is probably right!
            scores.append((target_phoneme, original_score))
            tar_i += 1
            gen_i += 1

        else: # check in case there are neighbouring letters which match, only look 2 letters ahead
            i = gen_i + 1
            VOWEL_CORRELATION_SIMILARITY_INDEX = 2
            found = False
            while i < len(phonemes) and i - gen_i <= VOWEL_CORRELATION_SIMILARITY_INDEX:
                score = score_phoneme_similarity(phonemes[i], target_phoneme)
                if score >= 3:
                    scores.append((target_phoneme, score))
                    tar_i += 1
                    gen_i = i
                    found = True
                    break  # exit loop
                i = i + 1

            if not found:
                scores.append((target_phonemes[tar_i], original_score))
                tar_i += 1

    print(scores)
    return scores


if __name__ == "__main__":
    phoneme_similarity()
# which_recognized_words()
