import chromadb
from sentence_transformers import SentenceTransformer

# Hinglish: RAG = pehle relevant context retrieve karo, phir LLM prompt me use karo.
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_database")
collection = client.get_or_create_collection(name="learning_notes")

question = "Which Python tool helps clean tabular data?"
query_embedding = model.encode([question]).tolist()
results = collection.query(query_embeddings=query_embedding, n_results=2)
context = "\n".join(results["documents"][0])

prompt = f"""
Use ONLY this context to answer.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

print(prompt)
