from WrdSmth.lemmatization import lemmatize_text

# Example 1: Lemmatization with automatic POS tagging
text1 = "These are some running dogs."
lemmas1 = lemmatize_text(text1)
print(lemmas1)
# Output: These be some run dog .

# Example 2: Lemmatization with provided POS tags
text2 = ["These", "are", "better", "examples"]
pos_tags = ['DT', 'VBP', 'JJR', 'NNS']  # Example POS tags
lemmas2 = lemmatize_text(text2, pos_tags=pos_tags)
print(lemmas2)
# Output: ['These', 'be', 'good', 'example']

# Example 3: Using a custom lemmatizer
def custom_lemmatizer(word):
    if word.endswith("ing"):
        return word[:-3]
    else:
        return word

text3 = "This is a custom lemmatization example."
lemmas3 = lemmatize_text(text3, lemmatizer_type='custom', custom_lemmatizer=custom_lemmatizer)
print(lemmas3)
# Output: This is a custom lemmatizati example.