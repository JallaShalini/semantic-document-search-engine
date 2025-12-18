MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

DATA_DIR = "data/raw_docs"
INDEX_DIR = "index"

EMBEDDINGS_PATH = "index/embeddings.npy"
METADATA_PATH = "index/metadata.json"
STATS_PATH = "index/index_stats.json"

BATCH_SIZE = 32
TOP_K = 5
SNIPPET_LENGTH = 200
