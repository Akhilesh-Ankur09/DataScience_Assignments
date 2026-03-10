import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download resources (only runs first time)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# -----------------------------
# INPUT TEXT (2 PARAGRAPHS)
# -----------------------------
text = """
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence! 
It enables computers to understand, interpret, and respond to human language. 
However, text data often contains noise: punctuation marks, stopwords, and other unnecessary elements.

Machine learning models work better when text is cleaned properly. 
Therefore, techniques such as stopword removal, stemming, and lemmatization are used in NLP pipelines. 
Can machines truly understand language? Researchers continue exploring this question!
"""

print("\n========== ORIGINAL TEXT ==========\n")
print(text)

# -----------------------------
# TOKENIZATION
# -----------------------------
tokens = word_tokenize(text)

print("\n========== TOKENS ==========\n")
print(tokens)

# -----------------------------
# REMOVE PUNCTUATION
# -----------------------------
tokens_no_punct = [word for word in tokens if word not in string.punctuation]

print("\n========== AFTER REMOVING PUNCTUATION ==========\n")
print(tokens_no_punct)

# -----------------------------
# STOPWORD REMOVAL
# -----------------------------
stop_words = set(stopwords.words('english'))

tokens_no_stop = [word for word in tokens_no_punct if word.lower() not in stop_words]

print("\n========== AFTER STOPWORD REMOVAL ==========\n")
print(tokens_no_stop)

# -----------------------------
# STEMMING
# -----------------------------
stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in tokens_no_stop]

print("\n========== AFTER STEMMING ==========\n")
print(stemmed_words)

# -----------------------------
# LEMMATIZATION
# -----------------------------
lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens_no_stop]

print("\n========== AFTER LEMMATIZATION ==========\n")
print(lemmatized_words)

# -----------------------------
# RECONSTRUCT CLEAN TEXT
# -----------------------------
clean_text = " ".join(lemmatized_words)

print("\n========== FINAL CLEANED TEXT ==========\n")
print(clean_text)