import re

def convert_to_utf8(ipa_string):
    result = ipa_string.encode('utf-8')
    print("utf-8:", result)
    return result

def convert_to_unicode(utf8_string):
    result = utf8_string.decode('utf-8')
    print("unicode:", result)
    return result

def check_IPA_pronunciation(ipa_word, original_word):
    utf8_string = convert_to_utf8(ipa_word)
    unicode_string = convert_to_unicode(utf8_string)
    array = re.split(r'(\[.*?\])', unicode_string)
    if len(array) >= 3:
        corrected_ipa_word = ''.join(array)  # Concatenate all elements to form the corrected IPA word
        print(f"You pronounced {array[1][1:-1]} of the word {original_word}({corrected_ipa_word}) wrong.")
    else:
        print("Invalid IPA format.")

# Example usage
check_IPA_pronunciation("frɔma[ʒ]", "fromage")
