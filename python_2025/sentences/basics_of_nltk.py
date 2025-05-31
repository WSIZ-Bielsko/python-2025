from nltk import pos_tag, word_tokenize
import nltk

"""
using nltk library

pip install nltk

"""

def setup_nltk():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')


def tag_sentence(sentence: str) -> list[tuple[str, str]]:
    # Tokenize and POS tag
    tokens = word_tokenize(sentence[:-1])  # Remove period for processing
    tagged = pos_tag(tokens)
    return tagged


if __name__ == '__main__':
    # setup_nltk()  # run this 1 time per interpreter
    sentence = 'The quick brown fox jumps over the lazy dog'

    tagged = tag_sentence(sentence)
    for word, tag in tagged:

        print(f'{word=}, {tag=}')


