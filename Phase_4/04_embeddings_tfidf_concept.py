# Install: python -m pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is useful for data analysis",
    "Machine learning uses data",
    "I love cooking Indian food",
    "Python can be used for artificial intelligence"
]
query = "Python and AI"

# Hinglish: TF-IDF modern AI embedding nahi hai, but vector/similarity concept samjhata hai.
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(vectors[-1], vectors[:-1])[0]
for doc, score in zip(documents, scores):
    print(round(score, 3), "->", doc)

print("Best match:", documents[scores.argmax()])
