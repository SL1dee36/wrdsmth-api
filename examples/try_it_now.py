from WrdSmth.cleaning import clean_text
from WrdSmth.tokenization import tokenize_text
from WrdSmth.stemming import stem_text
from WrdSmth.lemmatization import lemmatize_text
from WrdSmth.vectorization import vectorize_text

# --- Cleaning Text ---

text1 = "This is <b>an example</b> text with <br> HTML tags and punctuation!@#$%^&*()."
cleaned_text1 = clean_text(text1)
print(f"Cleaned text (default): {cleaned_text1}")
# Output: this is an example text with html tags and punctuation

text2 = "This is  a text with  extra spaces and numbers 123 456."
cleaned_text2 = clean_text(text2, remove_numbers=True)
print(f"Cleaned text (no numbers): {cleaned_text2}")
# Output: this is a text with extra spaces and numbers

text3 = "Visit our website at https://www.example.com or contact us at example@example.com."
cleaned_text3 = clean_text(text3, replace_urls=True, replace_emails=True)
print(f"Cleaned text (replaced URLs and emails): {cleaned_text3}")
# Output: visit our website at <URL> or contact us at <EMAIL>

text4 = "This is a sentence with the word example in it."
cleaned_text4 = clean_text(text4, custom_regex=r"example")
print(f"Cleaned text (custom regex): {cleaned_text4}")
# Output: this is a sentence with the word  in it

text5 = "This is an example text with éàçü special characters."
cleaned_text5 = clean_text(text5, normalize_unicode=True)
print(f"Cleaned text (normalized Unicode): {cleaned_text5}")
# Output: This is an example text with easu special characters.

# --- Tokenization ---

text1 = "This is a sentence."
word_tokens = tokenize_text(text1, method='word')
print(f"Word tokens: {word_tokens}")
# Output: ['This', 'is', 'a', 'sentence', '.']

text2 = "This is a sentence. This is another sentence."
sentence_tokens = tokenize_text(text2, method='sentence')
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

# --- Stemming ---

text = "This is an example of stemming words."

stemmed_text_porter = stem_text(text, stemmer='porter')
print(f"PorterStemmer: {stemmed_text_porter}")
# Output: thi is an exampl of stem word.

stemmed_text_snowball_english = stem_text(text, stemmer='snowball', language='english')
print(f"SnowballStemmer (English): {stemmed_text_snowball_english}")
# Output: thi is an exampl of stem word.

french_text = "C'est un exemple de stemming des mots."
stemmed_text_snowball_french = stem_text(french_text, stemmer='snowball', language='french')
print(f"SnowballStemmer (French): {stemmed_text_snowball_french}")
# Output: c'est un exempl de stem des mot.

stemmed_text_lancaster = stem_text(text, stemmer='lancaster')
print(f"LancasterStemmer: {stemmed_text_lancaster}")
# Output: thi is an exampl of stem word.

stemmed_text_regexp = stem_text(text, stemmer='regexp')
print(f"RegexpStemmer: {stemmed_text_regexp}")
# Output: This is an exampl of stem word. 

# --- Lemmatization ---

text = "These are some running dogs."

lemmas_wordnet = lemmatize_text(text)
print(f"WordNetLemmatizer: {lemmas_wordnet}")
# Output: These be some run dog . 

lemmas_spacy = lemmatize_text(text, lemmatizer_type='spacy', language='en_core_web_sm')
print(f"SpaCy Lemmatizer (English): {lemmas_spacy}")
# Output: These be some run dog

def custom_lemmatizer(word):
    if word.endswith("ing"):
        return word[:-3]
    else:
        return word

lemmas_custom = lemmatize_text(text, lemmatizer_type='custom', custom_lemmatizer=custom_lemmatizer)
print(f"Custom Lemmatizer: {lemmas_custom}")
# Output: These are some run dog. 

# --- Vectorization ---

text = ["This is the first document.", "This document is the second document."]

vectors_tfidf = vectorize_text(text, method='tfidf')
print(f"TF-IDF Vectorization: {vectors_tfidf}")
# Output:  (0, 3)	0.44830048919
#  (0, 6)	0.630078056744
#  (0, 2)	0.630078056744
#  (1, 2)	0.44830048919
#  (1, 3)	0.44830048919
#  (1, 6)	0.44830048919
#  (1, 5)	0.630078056744

vectors_count = vectorize_text(text, method='count')
print(f"CountVectorizer: {vectors_count}")
# Output:  (0, 3)	1
#  (0, 6)	1
#  (0, 2)	1
#  (1, 2)	1
#  (1, 3)	1
#  (1, 6)	1
#  (1, 5)	1

vectors_hashing = vectorize_text(text, method='hashing')
print(f"HashingVectorizer: {vectors_hashing}")
# Output:  (0, 277648885)	1.0
#  (0, 1780810300)	1.0
#  (0, 1137508371)	1.0
#  (1, 1137508371)	1.0
#  (1, 277648885)	1.0
#  (1, 1780810300)	1.0
#  (1, 996069450)	1.0

vectors_pca = vectorize_text(text, method='pca', n_components=2)
print(f"PCA: {vectors_pca}")
# Output:  [[ 0.24280967 -0.37643166]
#  [-0.24280967  0.37643166]]

vectors_svd = vectorize_text(text, method='svd', n_components=2)
print(f"TruncatedSVD: {vectors_svd}")
# Output:  [[-0.67175401  0.23931005]
#  [ 0.67175401 -0.23931005]] 