# -*- coding: utf-8 -*-

"""
Wrdsmth: A Python library for text preprocessing.
"""

__version__ = "0.1.0"

# Import main functions from other modules
from .cleaning import clean_text
from .tokenization import tokenize_text
from .stemming import stem_text
from .lemmatization import lemmatize_text
from .vectorization import vectorize_text