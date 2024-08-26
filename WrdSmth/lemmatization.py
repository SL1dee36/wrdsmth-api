# -*- coding: utf-8 -*-

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk, spacy

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from numba import njit

@njit
def lemmatize_text(text, pos_tags=None, lemmatizer_type='wordnet', custom_lemmatizer=None, language='english'):
    """
    Lemmatizes text using various lemmatizers and POS tag options.

    Args:
        text (str or list): Text or list of tokens to lemmatize.
        pos_tags (list, optional): List of part-of-speech tags for each token. 
                                    If None, POS tags will be determined automatically.
        lemmatizer_type (str, optional): Type of lemmatizer to use ('wordnet', 'spacy', 'custom'). Defaults to 'wordnet'.
        custom_lemmatizer (callable, optional): Custom lemmatizer function. Defaults to None.
        language (str, optional): Language of the text. Defaults to 'english'.

    Returns:
        str or list: Text or list of tokens with words reduced to their lemmas.
    """

    if lemmatizer_type == 'wordnet':
        lemmatizer = WordNetLemmatizer()
        if isinstance(text, str):
            tokens = text.split()
            if pos_tags is None:
                pos_tags = get_wordnet_pos_tags(tokens)
            lemmas = [lemmatizer.lemmatize(token, pos=tag) for token, tag in zip(tokens, pos_tags)]
            return ' '.join(lemmas)
        elif isinstance(text, list):
            if pos_tags is None:
                pos_tags = get_wordnet_pos_tags(text)
            return [lemmatizer.lemmatize(token, pos=tag) for token, tag in zip(text, pos_tags)]
        else:
            raise TypeError("Input text must be a string or a list of tokens.")
    elif lemmatizer_type == 'spacy':
        
        nlp = spacy.load(language)
        if isinstance(text, str):
            doc = nlp(text)
            return " ".join([token.lemma_ for token in doc])
        elif isinstance(text, list):
            return [token.lemma_ for token in nlp(" ".join(text))]
        else:
            raise TypeError("Input text must be a string or a list of tokens.")
    elif lemmatizer_type == 'custom' and custom_lemmatizer:
        if isinstance(text, str):
            tokens = text.split()
            return ' '.join([custom_lemmatizer(token) for token in tokens])
        elif isinstance(text, list):
            return [custom_lemmatizer(token) for token in text]
        else:
            raise TypeError("Input text must be a string or a list of tokens.")
    else:
        raise ValueError("Invalid lemmatizer type or missing custom lemmatizer function.")

def get_wordnet_pos_tags(tokens):
    """
    Determines part-of-speech tags for a list of tokens and converts them to a format 
    understandable by WordNetLemmatizer.

    Args:
        tokens (list): List of tokens.

    Returns:
        list: List of part-of-speech tags in WordNet format.
    """
    pos_tags = nltk.pos_tag(tokens)
    wordnet_tags = []
    for token, tag in pos_tags:
        if tag.startswith('J'):
            wordnet_tags.append(wordnet.ADJ)
        elif tag.startswith('V'):
            wordnet_tags.append(wordnet.VERB)
        elif tag.startswith('N'):
            wordnet_tags.append(wordnet.NOUN)
        elif tag.startswith('R'):
            wordnet_tags.append(wordnet.ADV)
        else:
            wordnet_tags.append(wordnet.NOUN)  # Default to noun
    return wordnet_tags