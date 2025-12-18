import json
import numpy as np

from src.config import *
from src.embedder import Embedder
from src.similarity import compute_similarity


def search(query, top_k=TOP_K):
    if not query.strip():
        raise ValueError("Query cannot be empty")

    # Load index
    embeddings = np.load(EMBEDDINGS_PATH)
    with open(METADATA_PATH, "r") as f:
        metadata = json.load(f)

    # Encode query
    embedder = Embedder(MODEL_NAME)
    query_vector = embedder.model.encode(query)

    # Compute similarity
    scores = compute_similarity(query_vector, embeddings)

    # Top-k results
    top_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "document": metadata[str(idx)]["filename"],
            "score": float(scores[idx]),
            "snippet": metadata[str(idx)]["snippet"]
        })

    return results


def batch_search(query_file):
    with open(query_file, "r") as f:
        queries = f.readlines()

    results = {}
    for query in queries:
        query = query.strip()
        if query:
            results[query] = search(query)

    return results
