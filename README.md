# Semantic Document Search Engine

## Objective
This project implements a **semantic document search engine** that retrieves documents based on **meaning and context** rather than exact keyword matching.  
It serves as a foundational information retrieval system and can be extended to advanced applications such as **Retrieval-Augmented Generation (RAG)**.

---

## Key Features
- Semantic indexing using transformer-based embeddings
- Cosine similarity–based ranking
- Top-k relevant document retrieval
- Batch query processing
- Efficient vector storage using NumPy
- Command-line interface (CLI)

---

## Project Structure
```text
semantic-document-search-engine/
├── data/
│   ├── raw_docs/              # Input text documents (≥100 .txt files)
│   ├── sample_queries.txt     # Batch queries
│
├── index/
│   ├── embeddings.npy         # Document embeddings
│   ├── metadata.json          # Filenames & snippets
│   └── index_stats.json       # Index statistics
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── embedder.py
│   ├── indexer.py
│   ├── similarity.py
│   ├── search.py
│   └── utils.py
│
├── main.py
├── requirements.txt
├── benchmark.md
├── evaluation_notes.md
└── README.md
