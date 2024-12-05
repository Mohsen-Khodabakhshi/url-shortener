from aioredis import Redis, ConnectionPool

from core.config import redis_config

redis_pool: ConnectionPool = ConnectionPool.from_url(
    url=redis_config.redis_url,
    decode_responses=redis_config.decode_responses,
    max_connections=redis_config.max_connections,
)


async def get_redis() -> Redis:
    return Redis(connection_pool=redis_pool)
