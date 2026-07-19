def filter_stale(nodes, now, grace_days=30):
    fresh = []
    for n in nodes:
        if n.metadata.get("valid_to") and \
           parse(n.metadata["valid_to"]) < now - timedelta(days=grace_days):
            continue  # versión caducada
        if n.metadata.get("superseded_by"):
            continue  # reemplazado por versión más reciente
        fresh.append(n)
    return fresh