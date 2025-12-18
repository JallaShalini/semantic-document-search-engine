from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(query_vec, doc_vectors):
    return cosine_similarity(query_vec.reshape(1, -1), doc_vectors)[0]
