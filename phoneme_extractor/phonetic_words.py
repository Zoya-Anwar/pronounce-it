import random
import nltk


def get_french_phonetic_words(desired_phoneme="a"):
    # Make sure you've downloaded and extracted the Lexique dataset
    lexique_file = '/Users/zoyaanwar/PycharmProjects/pronounce-it/phoneme_extractor/Lexique382.tsv'

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

        return random_entry


def get_english_phonetic_words(desired_phoneme="e"):
    # Define the path to your custom pronunciation dictionary file
    custom_dict_file = "/Users/zoyaanwar/PycharmProjects/pronounce-it/phoneme_extractor/CMU.in.IPA.txt"

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

        return random_entry


if __name__ == "__main__":
    get_english_phonetic_words("e")
    get_french_phonetic_words("e")
