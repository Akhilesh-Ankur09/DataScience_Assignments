from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

print("\n========== TEXT CLASSIFICATION ==========\n")

# Sample dataset (simple and clean)
texts = [
    "I love machine learning",
    "Artificial intelligence is amazing",
    "I enjoy coding in python",
    "This movie is terrible",
    "I hate slow systems",
    "This is a bad experience"
]

labels = [1, 1, 1, 0, 0, 0]  # 1 = Positive, 0 = Negative

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test)