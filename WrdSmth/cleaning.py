# -*- coding: utf-8 -*-

import re
import unicodedata

def clean_text(text, remove_html=True, remove_punctuation=True, lowercase=True,
               remove_extra_spaces=True, remove_numbers=False, replace_urls=False,
               replace_emails=False, custom_regex=None, normalize_unicode=False):
    """
    Cleans text by removing or replacing unwanted characters and patterns.

    Args:
        text (str): Text to be cleaned.
        remove_html (bool, optional): Remove HTML tags. Defaults to True.
        remove_punctuation (bool, optional): Remove punctuation. Defaults to True.
        lowercase (bool, optional): Convert text to lowercase. Defaults to True.
        remove_extra_spaces (bool, optional): Remove extra spaces. Defaults to True.
        remove_numbers (bool, optional): Remove numbers. Defaults to False.
        replace_urls (bool, optional): Replace URLs with a placeholder. Defaults to False.
        replace_emails (bool, optional): Replace email addresses with a placeholder. Defaults to False.
        custom_regex (str, optional): Custom regular expression pattern to remove. Defaults to None.
        normalize_unicode (bool, optional): Normalize Unicode characters. Defaults to False.

    Returns:
        str: Cleaned text.
    """

    if remove_html:
        text = re.sub(r'<[^>]+>', '', text)

    if remove_punctuation:
        text = re.sub(r'[^\w\s]', '', text)

    if lowercase:
        text = text.lower()

    if remove_numbers:
        text = re.sub(r'\d+', '', text)

    if replace_urls:
        text = re.sub(r'http\S+|www\S+|https\S+', '<URL>', text)

    if replace_emails:
        text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '<EMAIL>', text)

    if custom_regex:
        text = re.sub(custom_regex, '', text)

    if normalize_unicode:
        text = unicodedata.normalize('NFKC', text)

    if remove_extra_spaces:
        text = ' '.join(text.split())

    return text