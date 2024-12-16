from fastapi import APIRouter, Depends, status

from apps.shortener.schemas import ShortenUrlRequest, ShortenUrlResponse
from apps.shortener.controllers import shortener_controller

from services.db import get_session

shortener_router = APIRouter(
    tags=["Shortener"],
    prefix="/shortener",
)


@shortener_router.post(
    "",
    response_model=ShortenUrlResponse,
    status_code=status.HTTP_201_CREATED,
)
async def shorten(
    payload: ShortenUrlRequest,
    db=Depends(get_session),
):
    return await shortener_controller.shorten(
        db=db,
        payload=payload,
    )
