from backend.utils import model


def embed_query(query):
    return model.encode([query])


def retrieve_chunks(index, query_embedding, chunks, k=5):
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]