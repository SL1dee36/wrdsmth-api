# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from numba import njit
from initialization import init_nltk

init_nltk()

@njit
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
    elif method == 'count':
        vectorizer = CountVectorizer(**kwargs)
        return vectorizer.fit_transform(text)
    elif method == 'hashing':
        vectorizer = HashingVectorizer(**kwargs)
        return vectorizer.fit_transform(text)
    elif method == 'pca':
        vectorizer = PCA(**kwargs)
        return vectorizer.fit_transform(text)
    elif method == 'svd':
        vectorizer = TruncatedSVD(**kwargs)
        return vectorizer.fit_transform(text)
    else:
        raise ValueError(f"Unsupported vectorization method: {method}. Choose from 'tfidf', 'count', 'hashing', 'pca', or 'svd'.")