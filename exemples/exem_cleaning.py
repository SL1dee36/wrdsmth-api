from WrdSmth.cleaning import clean_text

# Example 1: Remove HTML tags and punctuation
text1 = "This is <b>an example</b> text with <br> HTML tags and punctuation!@#$%^&*()."
cleaned_text1 = clean_text(text1)
print(cleaned_text1)
# Output: this is an example text with html tags and punctuation

# Example 2: Remove numbers and extra spaces
text2 = "This is  a text with  extra spaces and numbers 123 456."
cleaned_text2 = clean_text(text2, remove_numbers=True)
print(cleaned_text2)
# Output: this is a text with extra spaces and numbers

# Example 3: Replace URLs and email addresses
text3 = "Visit our website at https://www.example.com or contact us at example@example.com."
cleaned_text3 = clean_text(text3, replace_urls=True, replace_emails=True)
print(cleaned_text3)
# Output: visit our website at <URL> or contact us at <EMAIL>

# Example 4: Custom regex to remove specific words
text4 = "This is a sentence with the word example in it."
cleaned_text4 = clean_text(text4, custom_regex=r"example")
print(cleaned_text4)
# Output: this is a sentence with the word  in it