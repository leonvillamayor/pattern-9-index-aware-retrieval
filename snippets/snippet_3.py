def reformulate(query: str, index_schema: dict) -> str:
    prompt = f"""
    Reescribe la consulta para el índice con esquema {index_schema}.
    Añade sinónimos del dominio, resuelve pronombres si hay historial,
    y emite filtros de metadata como filtros explícitos.
    Query: {query}
    """
    return llm.complete(prompt)