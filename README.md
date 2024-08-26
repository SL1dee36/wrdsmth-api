# WrdSmth: Your Python Text Preprocessing Toolkit

**WrdSmth** is a versatile Python library designed to simplify and streamline your text preprocessing workflow. Whether you're working on Natural Language Processing (NLP) tasks, data analysis, or machine learning projects, WrdSmth provides a comprehensive suite of tools to clean, transform, and prepare your text data for optimal results.

## Installation

Install `WrdSmth` using pip:

```bash
pip install WrdSmth
```

## Key Features

* **Cleaning:** Remove unwanted characters, HTML tags, punctuation, and extra whitespace.
* **Tokenization:** Split text into individual words or sentences.
* **Stemming:** Reduce words to their base form (stem).
* **Lemmatization:** Convert words to their canonical form (lemma).
* **Vectorization:** Transform text into numerical vectors using TF-IDF.

## Usage

### 1. Cleaning Text

The `clean_text` function provides various options for cleaning text data:

```python
from WrdSmth.cleaning import clean_text

text = "This is an example text with <br> HTML tags, punctuation!@#$%^&*(), numbers 123, a URL https://www.example.com and an email example@example.com."

# Clean text with all default options
cleaned_text = clean_text(text)
print(cleaned_text)
# Output: this is an example text with html tags numbers 123 a url httpwwwexamplecom and an email exampleexamplecom
```

**Parameters:**

* `text` (str): Text to be cleaned.
* `remove_html` (bool, optional): Remove HTML tags. Defaults to `True`.
* `remove_punctuation` (bool, optional): Remove punctuation. Defaults to `True`.
* `lowercase` (bool, optional): Convert text to lowercase. Defaults to `True`.
* `remove_extra_spaces` (bool, optional): Remove extra spaces. Defaults to `True`.
* `remove_numbers` (bool, optional): Remove numbers. Defaults to `False`.
* `replace_urls` (bool, optional): Replace URLs with a placeholder. Defaults to `False`.
* `replace_emails` (bool, optional): Replace email addresses with a placeholder. Defaults to `False`.
* `custom_regex` (str, optional): Custom regular expression pattern to remove. Defaults to `None`.

### 2. Tokenization

The `tokenize_text` function offers various tokenization methods:

```python
from WrdSmth.tokenization import tokenize_text

text = "This is a sentence. This is another sentence."

# Word tokenization
word_tokens = tokenize_text(text, method='word')
print(word_tokens)
# Output: ['This', 'is', 'a', 'sentence', '.', 'This', 'is', 'another', 'sentence', '.']

# Sentence tokenization
sentence_tokens = tokenize_text(text, method='sentence')
print(sentence_tokens)
# Output: ['This is a sentence.', 'This is another sentence.']
```

**Parameters:**

* `text` (str): Text to be tokenized.
* `method` (str, optional): Tokenization method ('word', 'sentence', 'regex', 'custom'). Defaults to 'word'.
* `language` (str, optional): Language of the text. Defaults to 'english'.
* `n_gram_range` (tuple, optional): Minimum and maximum n-gram lengths (for 'word' method). Defaults to (1, 1).
* `regex_pattern` (str, optional): Regular expression pattern for tokenization (for 'regex' method). Defaults to None.
* `remove_stopwords` (bool, optional): Whether to remove stop words. Defaults to False.
* `stopwords` (list, optional): List of stop words to remove. Defaults to None (uses NLTK's English stop words).
* `lowercase` (bool, optional): Whether to lowercase the tokens. Defaults to False.
* `custom_tokenizer` (callable, optional): Custom tokenizer function. Defaults to None.


### 3. Stemming

The `stem_text` function reduces words to their base form:

```python
from WrdSmth.stemming import stem_text

text = "This is an example of stemming words."

stemmed_text = stem_text(text)
print(stemmed_text)
# Output: thi is an exampl of stem word .
```

**Parameters:**

* `text` (str or list): Text or list of tokens to stem.
* `stemmer` (str, optional): Type of stemmer. Defaults to 'porter'.

### 4. Lemmatization

The `lemmatize_text` function converts words to their canonical form:

```python
from WrdSmth.lemmatization import lemmatize_text

text = "These are some running dogs."
lemmas = lemmatize_text(text)
print(lemmas)
# Output: These be some run dog .
```

**Parameters:**

* `text` (str or list): Text or list of tokens to lemmatize.
* `pos_tags` (list, optional): List of part-of-speech tags for each token. If None, POS tags will be determined automatically.
* `lemmatizer_type` (str, optional): Type of lemmatizer to use ('wordnet', 'custom'). Defaults to 'wordnet'.
* `custom_lemmatizer` (callable, optional): Custom lemmatizer function. Defaults to None.

### 5. Vectorization

The `vectorize_text` function transforms text into numerical vectors using TF-IDF:

```python
from WrdSmth.vectorization import vectorize_text

text = ["This is the first document.", "This document is the second document."]
vectors = vectorize_text(text)
print(vectors)
```

**Parameters:**

* `text` (str or list): Text or list of texts to vectorize.
* `method` (str, optional): Vectorization method. Defaults to 'tfidf'.
* `**kwargs`: Additional arguments for the selected vectorization method.

## Contributing

Contributions are welcome! Please see the [Contribution Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
