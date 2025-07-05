from sentence_transformers import SentenceTransformer
import numpy as np

# Load the same embedding model used in embedder.py
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def search_index(query, index, chunks, top_k=3):
    """
    Searches the FAISS index for top-k most relevant chunks to the query.

    Args:
        query (str): The user's question.
        index (faiss.IndexFlatL2): The FAISS index containing embedded chunks.
        chunks (List[str]): The original text chunks.
        top_k (int): Number of most relevant chunks to retrieve.

    Returns:
        List[str]: List of top-k most relevant chunks.
    """
    # Encode the query into an embedding
    query_embedding = embedder.encode([query], convert_to_numpy=True)

    # Search the index for the closest vectors
    distances, indices = index.search(query_embedding, top_k)

    # Fetch and return the corresponding text chunks
    return [chunks[i] for i in indices[0]]
