def hybrid_score(query_emb, query_text, node, alpha=0.7, beta=0.3):
    cos = cosine_similarity(query_emb, node.embedding)
    bm  = bm25_score(query_text, node.text)         # del índice BM25
    bm_norm = (bm - BM25_MIN) / (BM25_MAX - BM25_MIN + 1e-9)
    return alpha * cos + beta * bm_norm