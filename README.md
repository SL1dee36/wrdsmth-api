# WrdSmth: Your Python Text Preprocessing Toolkit

**WrdSmth** is a versatile Python library designed to simplify and streamline your text preprocessing workflow. Whether you're working on Natural Language Processing (NLP) tasks, data analysis, or machine learning projects, WrdSmth provides a comprehensive suite of tools to clean, transform, and prepare your text data for optimal results.

## Installation

Install `WrdSmth` using pip:

```bash
pip install WrdSmth
```

## Key Features

* **Cleaning:** Remove unwanted characters, HTML tags, punctuation, and extra whitespace. Offers options for Unicode normalization, number removal, URL/email replacement, and custom regular expressions.
* **Tokenization:** Split text into individual words or sentences. Supports language detection for accurate tokenization and stop word removal.  Provides options for N-gram generation, custom regex-based tokenization, and custom tokenizer functions.
* **Stemming:** Reduce words to their base form (stem) using various algorithms including PorterStemmer, SnowballStemmer, LancasterStemmer, and RegexpStemmer. Supports multiple languages. 
* **Lemmatization:** Convert words to their canonical form (lemma) using WordNetLemmatizer, SpaCy, or custom functions. Supports various languages.
* **Vectorization:** Transform text into numerical vectors using methods like TF-IDF, CountVectorizer, HashingVectorizer, PCA, and TruncatedSVD.

## Usage

**Before you start using WrdSmth, make sure you have the required NLTK resources downloaded:**

```bash
python -m nltk.downloader punkt wordnet averaged_perceptron_tagger stopwords punkt_tab
```

### 1. Cleaning Text

The `clean_text` function provides various options for cleaning text data. 

```python
from WrdSmth.cleaning import clean_text

text = "This is an example text with <br> HTML tags, punctuation!@#$%^&*(), numbers 123, a URL https://www.example.com and an email example@example.com."

# Clean text with all default options
cleaned_text = clean_text(text)
print(f"Cleaned text (default): {cleaned_text}")
# Output: this is an example text with html tags numbers 123 a url httpwwwexamplecom and an email exampleexamplecom

# Clean text and remove numbers
cleaned_text_no_numbers = clean_text(text, remove_numbers=True)
print(f"Cleaned text (no numbers): {cleaned_text_no_numbers}")
# Output: this is an example text with html tags a url httpwwwexamplecom and an email exampleexamplecom

# Clean text, replace URLs and emails
cleaned_text_replace = clean_text(text, replace_urls=True, replace_emails=True)
print(f"Cleaned text (replaced URLs and emails): {cleaned_text_replace}")
# Output: this is an example text with html tags numbers 123 a url <URL> and an email <EMAIL>

# Clean text with a custom regex to remove specific words
cleaned_text_custom = clean_text(text, custom_regex=r"example")
print(f"Cleaned text (custom regex): {cleaned_text_custom}")
# Output: this is an  text with html tags, punctuation!@#$%^&*(), numbers 123, a url https://www. .com and an email @ .com.

text5 = "This is an example text with éàçü special characters."
cleaned_text5 = clean_text(text5, normalize_unicode=True)
print(f"Cleaned text (normalized Unicode): {cleaned_text5}")
# Output: This is an example text with easu special characters. 
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

The `tokenize_text` function offers various tokenization methods, including language detection, N-gram generation, custom regex-based tokenization, and stop word removal.

```python
from WrdSmth.tokenization import tokenize_text

text = "This is a sentence. This is another sentence."

# Word tokenization
word_tokens = tokenize_text(text, method='word')
print(f"Word tokens: {word_tokens}")
# Output: ['This', 'is', 'a', 'sentence', '.', 'This', 'is', 'another', 'sentence', '.']

# Sentence tokenization
sentence_tokens = tokenize_text(text, method='sentence')
print(f"Sentence tokens: {sentence_tokens}")
# Output: ['This is a sentence.', 'This is another sentence.']

text3 = "This is a sentence."
bigrams = tokenize_text(text3, method='word', n_gram_range=(2, 2))
print(f"Bigrams: {bigrams}")
# Output: [('This', 'is'), ('is', 'a'), ('a', 'sentence')]

text4 = "This is a sentence with stop words."
tokens_without_stopwords = tokenize_text(text4, method='word', remove_stopwords=True)
print(f"Tokens without stop words: {tokens_without_stopwords}")
# Output: ['This', 'sentence', 'stop', 'words', '.']

# Tokenization for a different language (e.g., French)
french_text = "Ceci est une phrase. C'est une autre phrase."
french_word_tokens = tokenize_text(french_text, method='word', language='french')
print(f"French word tokens: {french_word_tokens}")
# Output: ['Ceci', 'est', 'une', 'phrase', '.', 'C', "'", 'est', 'une', 'autre', 'phrase', '.']
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

The `stem_text` function reduces words to their base form using different stemming algorithms.  It supports multiple languages and allows you to choose from various stemmers, including PorterStemmer, SnowballStemmer, LancasterStemmer, and a configurable RegexpStemmer.

```python
from WrdSmth.stemming import stem_text

text = "This is an example of stemming words."

# Using PorterStemmer
stemmed_text_porter = stem_text(text, stemmer='porter')
print(f"PorterStemmer: {stemmed_text_porter}")
# Output: thi is an exampl of stem word.

# Using SnowballStemmer for English
stemmed_text_snowball_english = stem_text(text, stemmer='snowball', language='english')
print(f"SnowballStemmer (English): {stemmed_text_snowball_english}")
# Output: thi is an exampl of stem word.

# Using SnowballStemmer for French
french_text = "C'est un exemple de stemming des mots."
stemmed_text_snowball_french = stem_text(french_text, stemmer='snowball', language='french')
print(f"SnowballStemmer (French): {stemmed_text_snowball_french}")
# Output: c'est un exempl de stem des mot.

# Using LancasterStemmer
stemmed_text_lancaster = stem_text(text, stemmer='lancaster')
print(f"LancasterStemmer: {stemmed_text_lancaster}")
# Output: thi is an exampl of stem word.

# Using RegexpStemmer
stemmed_text_regexp = stem_text(text, stemmer='regexp')
print(f"RegexpStemmer: {stemmed_text_regexp}")
# Output: This is an exampl of stem word. 
```

**Parameters:**

* `text` (str or list): Text or list of tokens to stem.
* `stemmer` (str, optional): Type of stemmer. Defaults to 'porter'. Choose from 'porter', 'snowball', 'lancaster', or 'regexp'.
* `language` (str, optional): Language of the text. Defaults to 'english'. Used for SnowballStemmer.


### 4. Lemmatization

The `lemmatize_text` function converts words to their canonical form, using various lemmatizers: WordNetLemmatizer, SpaCy, or custom functions.

```python
from WrdSmth.lemmatization import lemmatize_text

text = "These are some running dogs."

# Using WordNetLemmatizer
lemmas_wordnet = lemmatize_text(text)
print(f"WordNetLemmatizer: {lemmas_wordnet}")
# Output: These be some run dog . 

# Using SpaCy lemmatizer (for English)
lemmas_spacy = lemmatize_text(text, lemmatizer_type='spacy', language='en_core_web_sm')
print(f"SpaCy Lemmatizer (English): {lemmas_spacy}")
# Output: These be some run dog

def custom_lemmatizer(word):
    # Replace this with your custom logic
    if word.endswith("ing"):
        return word[:-3]
    else:
        return word

lemmas_custom = lemmatize_text(text, lemmatizer_type='custom', custom_lemmatizer=custom_lemmatizer)
print(f"Custom Lemmatizer: {lemmas_custom}")
# Output: These are some run dog. 
```

**Parameters:**

* `text` (str or list): Text or list of tokens to lemmatize.
* `pos_tags` (list, optional): List of part-of-speech tags for each token. If None, POS tags will be determined automatically.
* `lemmatizer_type` (str, optional): Type of lemmatizer to use ('wordnet', 'spacy', 'custom'). Defaults to 'wordnet'.
* `custom_lemmatizer` (callable, optional): Custom lemmatizer function. Defaults to None.
* `language` (str, optional): Language of the text. Defaults to 'english'. Used for SpaCy.

### 5. Vectorization

The `vectorize_text` function transforms text into numerical vectors using various vectorization methods: TF-IDF, CountVectorizer, HashingVectorizer, PCA, and TruncatedSVD.

```python
from WrdSmth.vectorization import vectorize_text

text = ["This is the first document.", "This document is the second document."]

# Using TF-IDF
vectors_tfidf = vectorize_text(text, method='tfidf')
print(f"TF-IDF Vectorization: {vectors_tfidf}")
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
print(f"CountVectorizer: {vectors_count}")
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
print(f"HashingVectorizer: {vectors_hashing}")
# Output:  
#  (0, 277648885)	1.0
#  (0, 1780810300)	1.0
#  (0, 1137508371)	1.0
#  (1, 1137508371)	1.0
#  (1, 277648885)	1.0
#  (1, 1780810300)	1.0
#  (1, 996069450)	1.0

# Using PCA (dimensionality reduction)
vectors_pca = vectorize_text(text, method='pca', n_components=2)
print(f"PCA: {vectors_pca}")
# Output:  
#  [[ 0.24280967 -0.37643166]
#  [-0.24280967  0.37643166]]

# Using TruncatedSVD (dimensionality reduction)
vectors_svd = vectorize_text(text, method='svd', n_components=2)
print(f"TruncatedSVD: {vectors_svd}")
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
