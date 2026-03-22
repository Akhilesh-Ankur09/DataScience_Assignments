import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize

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

print("\n========== BAG OF WORDS ==========\n")

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform([text])

print("Feature Names:\n", vectorizer.get_feature_names_out())
print("\nBoW Matrix:\n", bow_matrix.toarray())

print("\n========== TF-IDF ==========\n")

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform([text])

print("Feature Names:\n", tfidf.get_feature_names_out())
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())

print("\n========== WORD2VEC ==========\n")

# New input (200+ words)
text_w2v = """
Artificial intelligence is transforming industries across the world. 
Machine learning models are being used in healthcare, finance, and education. 
Natural language processing enables machines to understand human communication. 
Deep learning techniques have improved computer vision and speech recognition systems. 
Companies are investing heavily in AI technologies to improve efficiency and automation. 
Data plays a crucial role in training these models and improving their accuracy. 
Researchers are continuously working on making AI systems more reliable and ethical. 
Applications of AI include chatbots, recommendation systems, fraud detection, and predictive analytics. 
The future of artificial intelligence looks promising with continuous advancements in technology. 
However, challenges such as bias, data privacy, and interpretability still need to be addressed carefully.
"""

# Tokenize sentences
sentences = sent_tokenize(text_w2v)

# Convert sentences to word tokens
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train Word2Vec model
model = Word2Vec(tokenized_sentences, vector_size=50, window=3, min_count=1, workers=2)

# Similarity checks
print("\nSimilarity between 'ai' and 'technology':")
print(model.wv.similarity('ai', 'technology'))

print("\nSimilarity between 'data' and 'model':")
print(model.wv.similarity('data', 'models'))

print("\nMost similar words to 'ai':")
print(model.wv.most_similar('ai'))
