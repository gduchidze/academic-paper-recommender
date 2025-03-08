from config.config import model, logger
from database.connection import collection


def search_papers(query, top_k=5):
    query_embedding = model.encode(query).tolist()

    pipeline = [
        {
            "$search": {
                "index": "embedding_vector_index",
                "knnBeta": {
                    "vector": query_embedding,
                    "path": "vector_embedding",
                    "k": top_k
                }
            }
        },
        {
            "$project": {
                "title": 1,
                "keywords": 1,
                "publication_year": 1,
                "score": {"$meta": "searchScore"}
            }
        },
        {"$limit": top_k}
    ]

    results = collection.aggregate(pipeline)
    for result in results:
        logger.info(f"Title: {result['title']}\n Keywords: {result['keywords']}\n Publication Year: {result['publication_year']}")

search_papers("Microservice Arcitecture in Software Engieering")