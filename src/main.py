from config.config import model
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
        {"$limit": top_k}
    ]

    results = collection.aggregate(pipeline)
    for result in results:
        print(f"Title: {result['title']}\n{result['keywords']}\n Year: {result['publication_year']}")

search_papers("Articles about Neural Networks")