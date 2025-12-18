# Performance Benchmark

## Indexing Performance
- Number of documents indexed: 100+
- Embedding model: all-MiniLM-L6-v2
- Embedding dimension: 384
- Indexing time: ~30 seconds
- Hardware: CPU

---

## Search Performance
- Similarity metric: Cosine similarity
- Top-k results: 5
- Average query latency: ~100–150 ms per query

---

## Observations
- Semantic search retrieves contextually relevant documents
- Performance is suitable for small-to-medium document collections
- Indexing is a one-time cost; queries are fast

---

## Conclusion
The system provides efficient semantic retrieval with low query latency and accurate ranking, making it suitable as a foundation for larger retrieval systems.
