import time
from database.connection import collection
from database.redis import get_cache_key, get_cached_results, cache_results
from config.config import model


def find_similar_papers(query_embedding, top_k=5):
    query_embedding = model.encode(query_embedding).tolist()
    cache_key = get_cache_key(query_embedding, top_k)
    cached = get_cached_results(cache_key)
    if cached is not None:
        print("ქეშიდან მიღებული შედეგები.")
        return cached

    start_time = time.time()

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
                    "abstract": 1,
                    "publication_year": 1,
                    "score": {"$meta": "searchScore"}
                }
            }
        ]
    cursor = collection.aggregate(pipeline)
    results = list(cursor)

    elapsed_time = time.time() - start_time
    print(f"Search Result {elapsed_time:.4f} seconds.).")

    cache_results(cache_key, results)

    return results

print(find_similar_papers("Software Engineer", 5))