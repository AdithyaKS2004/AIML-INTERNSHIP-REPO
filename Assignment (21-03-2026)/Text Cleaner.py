# Build a Text Cleaner

import string

# Sample text
text = "Hello!!! This is a SIMPLE text, with punctuation and STOPWORDS."

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Remove stopwords
stopwords = ["is", "a", "and", "with"]
words = text.split()
cleaned_words = [word for word in words if word not in stopwords]

cleaned_text = " ".join(cleaned_words)

print("Cleaned Text:", cleaned_text)