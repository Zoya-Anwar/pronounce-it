import epitran
import string
from ipapy import UNICODE_TO_IPA

def get_phonemes_descriptors(phonemes):
    phoneme_objects = []
    for p in phonemes:
        phoneme_objects.append(UNICODE_TO_IPA[p])

    return phoneme_objects


def get_target_phonemes(target_sentence="manger"):
    epi = epitran.Epitran('fra-Latn-p')
    target = epi.transliterate(target_sentence.translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))
    target_phonemes = get_phonemes_descriptors(target)
    return target_phonemes




