import json, time
import numpy as np
from src.config import *
from src.document_loader import load_documents
from src.embedder import Embedder

def build_index():
    start = time.time()

    docs = load_documents(DATA_DIR)
    texts = [d["text"] for d in docs]

    embedder = Embedder(MODEL_NAME)
    embeddings = embedder.encode(texts, BATCH_SIZE)

    np.save(EMBEDDINGS_PATH, embeddings)

    metadata = {
        i: {
            "id": docs[i]["id"],
            "filename": docs[i]["filename"],
            "snippet": docs[i]["text"][:SNIPPET_LENGTH]
        }
        for i in range(len(docs))
    }

    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=2)

    stats = {
        "doc_count": len(docs),
        "dimension": embeddings.shape[1],
        "model": MODEL_NAME,
        "created_at": time.ctime()
    }

    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Index built in {time.time() - start:.2f}s")
