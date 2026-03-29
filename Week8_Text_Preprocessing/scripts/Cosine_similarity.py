from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

print("\n========== COSINE SIMILARITY ==========\n")

sentences = [
    "Artificial intelligence is transforming industries",
    "Machine learning is a part of artificial intelligence",
    "Cooking recipes require different ingredients"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

similarity_matrix = cosine_similarity(tfidf_matrix)

print("Cosine Similarity Matrix:\n")
print(similarity_matrix)