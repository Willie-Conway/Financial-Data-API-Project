# backend/app/services/cache.py

import redis
import os
import json
from typing import Optional, Any

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD", None),
    db=int(os.getenv("REDIS_DB", 0))
)

def get_from_cache(key: str) -> Optional[Any]:
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None

def set_in_cache(key: str, value: Any, expire: int = 3600) -> bool:
    try:
        redis_client.setex(key, expire, json.dumps(value))
        return True
    except Exception as e:
        print(f"Error setting cache: {e}")
        return False