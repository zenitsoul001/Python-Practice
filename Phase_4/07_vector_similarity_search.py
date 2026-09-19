import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_database")
collection = client.get_or_create_collection(name="learning_notes")

query = "How can I clean table data in Python?"
query_embedding = model.encode([query]).tolist()

results = collection.query(query_embeddings=query_embedding, n_results=2)

# Hinglish: Lower distance generally closer match ko indicate karti hai.
for doc, distance in zip(results["documents"][0], results["distances"][0]):
    print("Document:", doc)
    print("Distance:", round(distance, 4))
