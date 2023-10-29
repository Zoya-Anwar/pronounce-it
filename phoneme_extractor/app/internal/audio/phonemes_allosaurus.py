from allosaurus.app import read_recognizer


def get_phonemes(filename="./output.wav"):
    # load your model
    model = read_recognizer()

    # run inference -> æ l u s ɔ ɹ s
    inferences = model.recognize(filename, "fra")

    print("phonemes of audio recording:", inferences, "\n")

    return inferences


if __name__ == "__main__":
    get_phonemes()