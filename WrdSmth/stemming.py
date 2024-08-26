# -*- coding: utf-8 -*-

from nltk.stem.porter import PorterStemmer

def stem_text(text, stemmer='porter'):
    """
    Reduces words in text to their base form (stem).

    Args:
        text (str or list): Text or list of tokens to stem.
        stemmer (str, optional): Type of stemmer. Defaults to 'porter'.

    Returns:
        str or list: Text or list of tokens with words reduced to their base form.
    """
    if stemmer == 'porter':
        stemmer = PorterStemmer()
    else:
        raise ValueError("Unsupported stemmer type. Currently only 'porter' is supported.")

    if isinstance(text, str):
        tokens = text.split()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return ' '.join(stemmed_tokens)
    elif isinstance(text, list):
        return [stemmer.stem(token) for token in text]
    else:
        raise TypeError("Input text must be a string or a list of tokens.")