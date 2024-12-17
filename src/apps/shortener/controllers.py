import random

import string

from datetime import datetime, timedelta

from aioredis import Redis

from fastapi import HTTPException, status

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from apps.shortener.schemas import ShortenUrlRequest, ShortenUrlResponse
from apps.shortener.models import ShortenedUrl


class ShortenerController:
    @staticmethod
    def generate_random_characters(length: int) -> str:
        char_set = string.ascii_letters + string.digits
        return "".join(random.choice(char_set) for _ in range(length))

    async def shorten(
        self, db: AsyncSession, payload: ShortenUrlRequest
    ) -> ShortenUrlResponse:
        short_url = self.generate_random_characters(length=5)
        shortened_url = ShortenedUrl(
            main_url=payload.main_url,
            short_url=short_url,
            expires_at=datetime.timestamp(
                datetime.utcnow()
                + timedelta(hours=payload.expiration_time_month.value * 730),
            ),
        )
        db.add(shortened_url)
        await db.commit()
        return ShortenUrlResponse(
            main_url=payload.main_url,
            short_url=short_url,
        )

    @staticmethod
    async def redirect_to_main_url(
        db: AsyncSession, redis: Redis, short_url: str
    ) -> str:
        main_url = await redis.get(short_url)
        if main_url:
            return main_url

        statement = select(ShortenedUrl).where(ShortenedUrl.short_url == short_url)
        results = await db.exec(statement)
        shortened_url: ShortenedUrl = results.first()
        if not shortened_url:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="shortened url not found",
            )
        main_url = shortened_url.main_url

        await redis.set(
            name=short_url,
            value=main_url,
            ex=2 * 60,
        )

        return main_url


shortener_controller = ShortenerController()
