def compress_node(node, query, llm):
    prompt = f"""Extract only the sentences from the chunk that are
    directly relevant to answering the query. Preserve exact wording.
    Query: {query}
    Chunk: {node.text}
    Relevant spans:"""
    spans = llm.complete(prompt, max_tokens=node.text_tokens // 3)
    return Node(
        node_id=node.node_id,           # lineage intacto
        text=spans,
        metadata=node.metadata,         # authority, timestamp, etc.
        compression_ratio=len(spans) / len(node.text),
    )