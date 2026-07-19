# 1. Structural chunking: respeta headings, párrafos y tablas
structural_chunks = split_by_headers(doc, max_tokens=512)

# 2. Semantic chunking: subdivide los bloques grandes por cambio de tema
semantic_chunks = []
for chunk in structural_chunks:
    semantic_chunks.extend(
        split_by_embedding_distance(chunk, threshold=0.3, min_tokens=128)
    )