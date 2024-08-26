# -*- coding: utf-8 -*-

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import LancasterStemmer, RegexpStemmer

def stem_text(text, stemmer='porter', language='english'):
    """
    Reduces words in text to their base form (stem) using various stemmer algorithms.

    Args:
        text (str or list): Text or list of tokens to stem.
        stemmer (str, optional): Type of stemmer. Defaults to 'porter'.
        language (str, optional): Language of the text. Defaults to 'english'.

    Returns:
        str or list: Text or list of tokens with words reduced to their base form.
    """

    if stemmer == 'porter':
        stemmer = PorterStemmer()
    elif stemmer == 'snowball':
        stemmer = SnowballStemmer(language)
    elif stemmer == 'lancaster':
        stemmer = LancasterStemmer()
    elif stemmer == 'regexp':
        stemmer = RegexpStemmer(r'ing$|s$|ed$|ies$', min=3)  # Example regexp stemmer
    else:
        raise ValueError(f"Unsupported stemmer type: {stemmer}. Choose from 'porter', 'snowball', 'lancaster', or 'regexp'.")

    if isinstance(text, str):
        tokens = text.split()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return ' '.join(stemmed_tokens)
    elif isinstance(text, list):
        return [stemmer.stem(token) for token in text]
    else:
        raise TypeError("Input text must be a string or a list of tokens.")