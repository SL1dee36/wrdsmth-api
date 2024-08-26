# -*- coding: utf-8 -*-

import nltk
from nltk.util import ngrams

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def tokenize_text(text, method='word', language='english', n_gram_range=(1, 1),
                  regex_pattern=None, remove_stopwords=False, stopwords=None, lowercase=False,
                  custom_tokenizer=None):
    """
    Tokenizes text using various methods, language options, and advanced features.

    Args:
        text (str): Text to be tokenized.
        method (str, optional): Tokenization method ('word', 'sentence', 'regex', 'custom'). Defaults to 'word'.
        language (str, optional): Language of the text. Defaults to 'english'.
        n_gram_range (tuple, optional): Minimum and maximum n-gram lengths (for 'word' method). Defaults to (1, 1).
        regex_pattern (str, optional): Regular expression pattern for tokenization (for 'regex' method). Defaults to None.
        remove_stopwords (bool, optional): Whether to remove stop words. Defaults to False.
        stopwords (list, optional): List of stop words to remove. Defaults to None (uses NLTK's English stop words).
        lowercase (bool, optional): Whether to lowercase the tokens. Defaults to False.
        custom_tokenizer (callable, optional): Custom tokenizer function. Defaults to None.

    Returns:
        list: A list of tokens (words or sentences) depending on the chosen method.
    """

    if method == 'word':
        tokens = nltk.word_tokenize(text, language=language)
        if lowercase:
            tokens = [token.lower() for token in tokens]
        if n_gram_range != (1, 1):
            tokens = list(ngrams(tokens, *n_gram_range))
    elif method == 'sentence':
        tokens = nltk.sent_tokenize(text, language=language)
    elif method == 'regex' and regex_pattern:
        tokens = nltk.regexp_tokenize(text, regex_pattern)
    elif method == 'custom' and custom_tokenizer:
        tokens = custom_tokenizer(text)
    else:
        raise ValueError("Invalid tokenization method or missing parameters.")

    if remove_stopwords:
        if stopwords is None:
            stopwords = nltk.corpus.stopwords.words('english')
        tokens = [token for token in tokens if token not in stopwords]

    return tokens