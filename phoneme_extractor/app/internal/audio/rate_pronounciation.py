import speech_recognition as sr
from nltk.tokenize import word_tokenize
from app.internal.audio.phonemes_allosaurus import get_phonemes
import epitran
import string
from ipapy import UNICODE_TO_IPA


def which_recognized_words(target_sentence="avons", file_name="output.wav"):
    target_tokens = word_tokenize(target_sentence.lower())

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Recognize the speech from the provided WAV file
    with sr.AudioFile(file_name) as source:
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


def get_target_generated_phonemes(phrase, input_file):
    # get generated phonemes
    generated = get_phonemes(filename=input_file).replace(" ", "")
    phonemes = get_phonemes_descriptors(generated)

    # get target phonemes
    epi = epitran.Epitran('fra-Latn-p')
    target = epi.transliterate(phrase.translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))
    target_phonemes = get_phonemes_descriptors(target)

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


def phoneme_similarity(target_sentence="avons", input_file="output.wav"):

    phonemes, target_phonemes = get_target_generated_phonemes(target_sentence, input_file)

    s = str(target_sentence.translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))
    print(s)


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
                    gen_i += 1
                    found = True
                    break  # exit loop
                i = i + 1

            if not found:
                scores.append((target_phonemes[tar_i], original_score))
                tar_i += 1

    print()
    for item in scores:
        print(f"score:{item[1]}       letter: {item[0]}")

    # Convert IPAVowel objects to string before JSON serialization
    min(len(s), len(scores))
    data = [{"score": scores[i][1], "letter": f"{s[i]}"} for i in range(min(len(s), len(scores)))]

    # sample json-ified output for:
    # score:4       phoneme: a
    # score:1       phoneme: v
    # score:4       phoneme: ɔ
    # score:1       phoneme: ̃
    #
    # [
    #     {
    #         "score": 4,
    #         "phoneme": "a"
    #     },
    #     {
    #         "score": 1,
    #         "phoneme": "v"
    #     },
    #     {
    #         "score": 4,
    #         "phoneme": "\u0254"
    #     },
    #     {
    #         "score": 1,
    #         "phoneme": "\u0303"
    #     }
    # ]
    #
    # will need to re convert the unicode characters to IPA characters in front end


    # String builder
    delimeter_result = ""
    for item in data:
        if item["score"] == 0:
            delimeter_result += f"[{str(item['letter'])}]"
        else:
            delimeter_result += str(item['letter'])

    print("letter added:", delimeter_result)
    print("data:", data)

    print(data)

    return scores, {"result": delimeter_result}


if __name__ == "__main__":
    phoneme_similarity("bonjour")
# which_recognized_words(target_tokens)
