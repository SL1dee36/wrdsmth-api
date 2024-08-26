from WrdSmth.tokenization import tokenize_text

# Example 1: Word tokenization
text1 = "This is a sentence."
word_tokens = tokenize_text(text1, method='word')
print(word_tokens)
# Output: ['This', 'is', 'a', 'sentence', '.']

# Example 2: Sentence tokenization
text2 = "This is a sentence. This is another sentence."
sentence_tokens = tokenize_text(text2, method='sentence')
print(sentence_tokens)
# Output: ['This is a sentence.', 'This is another sentence.']

# Example 3: N-gram tokenization (bigrams)
text3 = "This is a sentence."
bigrams = tokenize_text(text3, method='word', n_gram_range=(2, 2))
print(bigrams)
# Output: [('This', 'is'), ('is', 'a'), ('a', 'sentence')]

# Example 4: Tokenization with stop word removal
text4 = "This is a sentence with stop words."
tokens_without_stopwords = tokenize_text(text4, method='word', remove_stopwords=True)
print(tokens_without_stopwords)
# Output: ['This', 'sentence', 'stop', 'words', '.']