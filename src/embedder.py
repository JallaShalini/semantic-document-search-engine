from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import numpy as np

class Embedder:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts, batch_size):
        embeddings = []
        for i in tqdm(range(0, len(texts), batch_size)):
            batch = texts[i:i + batch_size]
            emb = self.model.encode(batch, show_progress_bar=False)
            embeddings.append(emb)
        return np.vstack(embeddings)
