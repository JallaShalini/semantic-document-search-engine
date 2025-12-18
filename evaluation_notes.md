# Evaluation Notes – Semantic Document Search Engine

## Why Semantic Search Over Keyword Search
Keyword-based search depends on exact word matches and fails when:
- Synonyms are used
- The same concept is expressed differently
- Query intent is conceptual

Semantic search solves these issues by understanding **meaning and context**.

---

## Methodology Used
- Documents are converted into dense vector embeddings
- Queries are embedded using the same model
- Cosine similarity measures semantic closeness
- Results are ranked by similarity score

---

## Embedding Model Selection
The **all-MiniLM-L6-v2** model is chosen because:
- It provides high-quality semantic representations
- It is computationally efficient
- It is widely used in industry and research

---

## Similarity Metric
**Cosine similarity** is used because it:
- Works well in high-dimensional spaces
- Measures directional similarity
- Is standard for semantic retrieval systems

---

## Design Decisions
- NumPy arrays for efficient vector storage
- JSON metadata for readability and separation of concerns
- Modular architecture for extensibility
- Batch processing for scalability

---

## Limitations
- Exact similarity search scales linearly with data size
- Not optimized for very large datasets

---

## Future Improvements
- FAISS-based ANN search
- RAG integration
- Document chunking
- Web interface

---

## Conclusion
This project demonstrates a robust semantic search pipeline that retrieves documents based on **meaning rather than keywords**, offering higher relevance and extensibility.
