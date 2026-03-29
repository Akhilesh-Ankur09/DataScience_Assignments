# Week 8 – NLP Text Preprocessing & Feature Engineering

## Objective
To implement text preprocessing techniques and feature engineering methods used in Natural Language Processing (NLP).

---

## Assignment 1 – Text Preprocessing

### Input
Two paragraphs containing multiple punctuation marks such as:
., : ; ! ?

### Techniques Implemented

1. **Tokenization**
2. **Punctuation Removal**
3. **Stop Word Removal**
4. **Stemming**
5. **Lemmatization**

### Description
- The input text is first tokenized into individual words.
- Punctuation marks are removed using Python's `string` module.
- Stop words are removed using NLTK's stopword corpus.
- Stemming is performed using `PorterStemmer`.
- Lemmatization is performed using `WordNetLemmatizer`.
- A final cleaned text is reconstructed for better understanding.

---

## Assignment 2 – Feature Engineering

### Techniques Implemented

### 1. Bag of Words (BoW)
- Converts text into a numerical representation based on word frequency.
- Implemented using `CountVectorizer` from Scikit-learn.

### 2. TF-IDF (Term Frequency – Inverse Document Frequency)
- Assigns importance to words based on frequency and uniqueness.
- Implemented using `TfidfVectorizer`.

---

## Word2Vec Implementation

### Input
A separate paragraph containing more than 200 words related to Artificial Intelligence.

### Steps Performed
- Sentence tokenization using NLTK
- Word tokenization and lowercase conversion
- Training Word2Vec model using Gensim
- Generating word embeddings

### Similarity Analysis
- Calculated similarity between words such as:
  - 'ai' and 'technology'
  - 'data' and 'models'
- Retrieved most similar words using:
  ```python
  model.wv.most_similar('ai')
  
## Additional NLP Tasks

### Cosine Similarity
- Computed similarity between three sentences using TF-IDF vectors.

### Text Classification (Supervised Learning)
- Implemented using Multinomial Naive Bayes.
- Classified text into positive and negative categories.

### Text Clustering (Unsupervised Learning)
- Implemented using K-Means clustering.
- Grouped similar documents into clusters based on content similarity.
  
### Tools & Libraries Used
Python
NLTK
Scikit-learn
Gensim
PyCharm
GitHub
Output
Cleaned and processed text
Feature vectors using BoW and TF-IDF
Word embeddings using Word2Vec
Similarity scores between selected words


### Author

Akhilesh Ankur