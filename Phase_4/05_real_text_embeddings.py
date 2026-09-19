# Install: python -m pip install sentence-transformers scikit-learn
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Hinglish: First run par model internet se download ho sakta hai.
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is a programming language.",
    "I enjoy coding in Python.",
    "The weather is sunny today."
]

embeddings = model.encode(sentences)
print("Embedding dimensions:", len(embeddings[0]))

score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
print("Similarity:", round(float(score), 3))
