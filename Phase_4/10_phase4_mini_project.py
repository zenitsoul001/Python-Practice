# Install: python -m pip install chromadb sentence-transformers
import chromadb
from sentence_transformers import SentenceTransformer

# Hinglish: Local semantic search app
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./mini_project_db")
collection = client.get_or_create_collection(name="python_lessons")

documents = [
    "Python files can be opened using the open function.",
    "JSON is commonly used for exchanging API data.",
    "Pandas DataFrames are useful for tabular data analysis.",
    "GET requests retrieve information from APIs.",
    "POST requests send data to APIs.",
    "Embeddings convert text into numerical vectors.",
    "Vector databases store and search embeddings."
]
ids = [f"lesson_{i}" for i in range(1, len(documents)+1)]
collection.upsert(ids=ids, documents=documents, embeddings=model.encode(documents).tolist())

while True:
    query = input("Question likho (exit to close): ").strip()
    if query.lower() == "exit":
        break

    results = collection.query(query_embeddings=model.encode([query]).tolist(), n_results=3)
    print("\nRelevant lessons:")
    for i, doc in enumerate(results["documents"][0], start=1):
        print(f"{i}. {doc}")
    print()
