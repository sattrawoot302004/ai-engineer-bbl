from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

with open(
    "knowledge_base.txt",
    "r",
    encoding="utf-8",
) as file:
    text = file.read()

chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

# print (chunks)
chunk_embeddings = embedding_model.encode(chunks)

def search_knowledge_base(
    query: str,
    top_k: int = 3,
) -> list[str]:
    query_embedding = embedding_model.encode(query)

    similarities = embedding_model.similarity(
        query_embedding,
        chunk_embeddings,
    )[0]

    ranked_indices = similarities.argsort(
        descending=True,
    )[:top_k]

    return [
        chunks[index]
        for index in ranked_indices
    ]