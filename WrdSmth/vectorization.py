# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(text, method='tfidf', **kwargs):
    """
    Converts text into a numerical vector.

    Args:
        text (str or list): Text or list of texts to vectorize.
        method (str, optional): Vectorization method. Defaults to 'tfidf'.
        **kwargs: Additional arguments for the selected vectorization method.

    Returns:
        array-like or sparse matrix: Vector representation of the text.
    """
    if method == 'tfidf':
        vectorizer = TfidfVectorizer(**kwargs)
        return vectorizer.fit_transform(text)
    else:
        raise ValueError("Unsupported vectorization method. Currently only 'tfidf' is supported.")