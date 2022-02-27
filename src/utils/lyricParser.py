import re 
import en_core_web_sm
import string
import json

from spacy.lang.en.stop_words import STOP_WORDS

def tokenizeLyrics(lyrics, nlp):
    

    text = re.sub("[\[].*?[\]]", "", lyrics)

    # load the text into spacy
    document = nlp(text)

    # tokenize
    tokens = [word.text for word in document]

    # lowercase EVERYTHING
    tokens_lower = [token.lower() for token in tokens]

    # Make a table that translates all punctuation to an empty value (`None`)
    table = str.maketrans('', '', string.punctuation)
    # punc_table = {chr(key):value for (key, value) in table.items()}

    tokens_nopunct = [token.translate(table) for token in tokens_lower]

    # remove "None" from the tokens
    tokens_notempty = [token for token in tokens_nopunct if token != '']

    # remove single characters 
    tokens_noSingleLetters = [token for token in tokens_notempty if len(token) >1 ]

    # remove escape squences & numbers
    tokens = [token for token in tokens_noSingleLetters if token.isalpha()]

    # import stopwords
    stopwords = [stop for stop in STOP_WORDS]

    # remove stopwords
    tokens_nostops = [token for token in tokens if token not in stopwords]

    return tokens_nostops
