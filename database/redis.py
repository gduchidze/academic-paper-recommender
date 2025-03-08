import redis, hashlib, pickle

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cache_key(query_embedding, method, top_k):

    embedding_str = ",".join(f"{x:.5f}" for x in query_embedding)
    key_str = f"{embedding_str}_{method}_{top_k}"
    return hashlib.md5(key_str.encode()).hexdigest()

def cache_results(cache_key, results, expiration=3600):
    redis_client.set(cache_key, pickle.dumps(results), ex=expiration)

def get_cached_results(cache_key):
    data = redis_client.get(cache_key)
    if data is not None:
        return pickle.loads(data)
    return None