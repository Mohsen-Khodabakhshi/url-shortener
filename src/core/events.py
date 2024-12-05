from services.redis import redis_pool
from services.db import engine


async def startup_event_handler() -> None:
    pass


async def shutdown_event_handler() -> None:
    await redis_pool.disconnect()
    await engine.dispose()
