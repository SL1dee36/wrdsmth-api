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

The `clean_text` function provides various options for cleaning text data. 

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
* `normalize_unicode` (bool, optional): Normalize Unicode characters. Defaults to `False`.


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
* `language` (str, optional): Language of the text. Defaults to 'english'. If None, the language will be detected automatically.
* `n_gram_range` (tuple, optional): Minimum and maximum n-gram lengths (for 'word' method). Defaults to (1, 1).
* `regex_pattern` (str, optional): Regular expression pattern for tokenization (for 'regex' method). Defaults to None.
* `remove_stopwords` (bool, optional): Whether to remove stop words. Defaults to False.
* `stopwords` (list, optional): List of stop words to remove. Defaults to None (uses NLTK's English stop words).
* `lowercase` (bool, optional): Whether to lowercase the tokens. Defaults to False.
* `custom_tokenizer` (callable, optional): Custom tokenizer function. Defaults to None.


### 3. Stemming

The `stem_text` function reduces words to their base form using different stemming algorithms:

```python
from WrdSmth.stemming import stem_text

text = "This is an example of stemming words."

# Using PorterStemmer
stemmed_text_porter = stem_text(text, stemmer='porter')
print(stemmed_text_porter)
# Output: thi is an exampl of stem word.

# Using SnowballStemmer for English
stemmed_text_snowball_english = stem_text(text, stemmer='snowball', language='english')
print(stemmed_text_snowball_english)
# Output: thi is an exampl of stem word.

# Using SnowballStemmer for French
french_text = "C'est un exemple de stemming des mots."
stemmed_text_snowball_french = stem_text(french_text, stemmer='snowball', language='french')
print(stemmed_text_snowball_french)
# Output: c'est un exempl de stem des mot.

# Using LancasterStemmer
stemmed_text_lancaster = stem_text(text, stemmer='lancaster')
print(stemmed_text_lancaster)
# Output: thi is an exampl of stem word.

# Using RegexpStemmer
stemmed_text_regexp = stem_text(text, stemmer='regexp')
print(stemmed_text_regexp)
# Output: This is an exampl of stem word. 
```

**Parameters:**

* `text` (str or list): Text or list of tokens to stem.
* `stemmer` (str, optional): Type of stemmer. Defaults to 'porter'. Choose from 'porter', 'snowball', 'lancaster', or 'regexp'.
* `language` (str, optional): Language of the text. Defaults to 'english'. Used for SnowballStemmer.


### 4. Lemmatization

The `lemmatize_text` function converts words to their canonical form, using various lemmatizers:

```python
from WrdSmth.lemmatization import lemmatize_text

text = "These are some running dogs."

# Using WordNetLemmatizer
lemmas_wordnet = lemmatize_text(text)
print(lemmas_wordnet)
# Output: These be some run dog . 

# Using SpaCy lemmatizer (for English)
lemmas_spacy = lemmatize_text(text, lemmatizer_type='spacy', language='en_core_web_sm')
print(lemmas_spacy)
# Output: These be some run dog

# Using a custom lemmatizer (example)
def custom_lemmatizer(word):
    # Replace this with your custom logic
    if word.endswith("ing"):
        return word[:-3]
    else:
        return word

lemmas_custom = lemmatize_text(text, lemmatizer_type='custom', custom_lemmatizer=custom_lemmatizer)
print(lemmas_custom)
# Output: These are some run dog. 
```

**Parameters:**

* `text` (str or list): Text or list of tokens to lemmatize.
* `pos_tags` (list, optional): List of part-of-speech tags for each token. If None, POS tags will be determined automatically.
* `lemmatizer_type` (str, optional): Type of lemmatizer to use ('wordnet', 'spacy', 'custom'). Defaults to 'wordnet'.
* `custom_lemmatizer` (callable, optional): Custom lemmatizer function. Defaults to None.
* `language` (str, optional): Language of the text. Defaults to 'english'. Used for SpaCy.

### 5. Vectorization

The `vectorize_text` function transforms text into numerical vectors using various vectorization methods:

```python
from WrdSmth.vectorization import vectorize_text

text = ["This is the first document.", "This document is the second document."]

# Using TF-IDF
vectors_tfidf = vectorize_text(text, method='tfidf')
print(vectors_tfidf)
# Output:
#  (0, 3)	0.44830048919
#  (0, 6)	0.630078056744
#  (0, 2)	0.630078056744
#  (1, 2)	0.44830048919
#  (1, 3)	0.44830048919
#  (1, 6)	0.44830048919
#  (1, 5)	0.630078056744

# Using CountVectorizer
vectors_count = vectorize_text(text, method='count')
print(vectors_count)
# Output:
#  (0, 3)	1
#  (0, 6)	1
#  (0, 2)	1
#  (1, 2)	1
#  (1, 3)	1
#  (1, 6)	1
#  (1, 5)	1

# Using HashingVectorizer
vectors_hashing = vectorize_text(text, method='hashing')
print(vectors_hashing)
# Output:  
#  (0, 277648885)	1.0
#  (0, 1780810300)	1.0
#  (0, 1137508371)	1.0
#  (1, 1137508371)	1.0
#  (1, 277648885)  	1.0
#  (1, 1780810300)	1.0
#  (1, 996069450)	1.0

# Using PCA (dimensionality reduction)
vectors_pca = vectorize_text(text, method='pca', n_components=2)
print(vectors_pca)
# Output:  
#  [[ 0.24280967 -0.37643166]
#  [-0.24280967  0.37643166]]

# Using TruncatedSVD (dimensionality reduction)
vectors_svd = vectorize_text(text, method='svd', n_components=2)
print(vectors_svd)
# Output:  
#  [[-0.67175401  0.23931005]
#  [ 0.67175401 -0.23931005]] 
```

**Parameters:**

* `text` (str or list): Text or list of texts to vectorize.
* `method` (str, optional): Vectorization method. Defaults to 'tfidf'. Choose from 'tfidf', 'count', 'hashing', 'pca', or 'svd'.
* `**kwargs`: Additional arguments for the selected vectorization method.

## Contributing

Contributions are welcome! Please see the [Contribution Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
