# Install: python -m pip install chromadb sentence-transformers
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_database")
collection = client.get_or_create_collection(name="learning_notes")

documents = [
    "Python is useful for data analysis.",
    "Pandas helps clean tabular data.",
    "Vector databases store embeddings."
]
ids = ["doc1", "doc2", "doc3"]
embeddings = model.encode(documents).tolist()

# Hinglish: upsert insert ya update dono handle karta hai.
collection.upsert(ids=ids, documents=documents, embeddings=embeddings)
print("Documents ChromaDB me save ho gaye.")
