from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

print("\n========== TEXT CLUSTERING ==========\n")

documents = [
    "AI is transforming the world",
    "Machine learning improves systems",
    "Deep learning is a subset of AI",
    "Football is a popular sport",
    "Cricket is widely played",
    "Sports bring people together"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X)

for i, doc in enumerate(documents):
    print(f"Document: {doc}")
    print(f"Cluster: {clusters[i]}")
    print()