from config.config import model, logger
from database.connection import collection
from typing import List, Dict, Any
import time


def search_papers(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    start_time = time.time()

    try:
        cleaned_query = query.strip()
        if not cleaned_query:
            logger.warning("ცარიელი საძიებო მოთხოვნა მოწოდებულია")
            return []

        query_embedding = model.encode(cleaned_query).tolist()

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
            # {
            #     "$project": {
            #         "title": 1,
            #         "keywords": 1,
            #         "publication_year": 1,
            #         "score": {"$meta": "searchScore"}
            #     }

            {"$limit": top_k}
        ]

        results = list(collection.aggregate(pipeline))

        elapsed_time = time.time() - start_time
        logger.info(f"ძიება დასრულდა {elapsed_time:.2f} წამში, ნაპოვნია {len(results)} შედეგი")

        for i, result in enumerate(results, 1):
            logger.info(
                f"შედეგი #{i}:\n"
                f"  სათაური: {result.get('title', 'N/A')}\n"
                f"  საკვანძო სიტყვები: {result.get('keywords', [])}\n"
                f"  წელი: {result.get('publication_year', 'N/A')}\n"
                f"  Score: {result.get('score', 0):.4f}"
            )

        return results
    except Exception as e:
        logger.error(f"ძიების შესრულებისას შეცდომა მოხდა: {str(e)}")
        return []


if __name__ == "__main__":
    search_papers("Phenomelogy")