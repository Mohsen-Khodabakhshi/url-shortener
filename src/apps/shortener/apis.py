from aioredis import Redis

from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

from apps.shortener.schemas import ShortenUrlRequest, ShortenUrlResponse
from apps.shortener.controllers import shortener_controller

from services.db import get_session
from services.redis import get_redis

shortener_router = APIRouter(
    tags=["Shortener"],
    prefix="",
)


@shortener_router.post(
    "/shorten",
    response_model=ShortenUrlResponse,
    status_code=status.HTTP_201_CREATED,
)
async def shorten(
    payload: ShortenUrlRequest,
    db: AsyncSession = Depends(get_session),
):
    return await shortener_controller.shorten(
        db=db,
        payload=payload,
    )


@shortener_router.get(
    "/{short_url}",
    response_class=RedirectResponse,
    status_code=status.HTTP_302_FOUND,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Shortened url, not found | expired | deactivated."
        },
    },
)
async def redirect_to_main_url(
    short_url: str,
    db: AsyncSession = Depends(get_session),
    redis: Redis = Depends(get_redis),
):
    return await shortener_controller.redirect_to_main_url(
        db=db,
        redis=redis,
        short_url=short_url,
    )
