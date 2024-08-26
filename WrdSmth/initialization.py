# -*- coding: utf-8 -*-

import nltk
import pkg_resources

def init_nltk():
    """
    Проверяет, установлены ли необходимые данные NLTK, и если нет, то загружает их.
    """
    
    required_resources = ['punkt', 'punkt_tab', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']

    for resource in required_resources:
        try:
            pkg_resources.resource_exists('nltk', f'tokenizers/punkt/{resource}')
        except FileNotFoundError:
            print(f"Загрузка ресурса NLTK: {resource}")
            nltk.download(resource)