import random

import string

from datetime import datetime, timedelta

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


shortener_controller = ShortenerController()
