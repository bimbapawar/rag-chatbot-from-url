from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model only once
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def create_vector_store(chunks):
    """
    Embeds text chunks and stores them in a FAISS index.

    Args:
        chunks (List[str]): List of text chunks.

    Returns:
        Tuple[faiss.IndexFlatL2, List[str]]: FAISS index and corresponding chunks.
    """
    # Generate embeddings for each chunk
    embeddings = embedder.encode(chunks, convert_to_numpy=True)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, chunks
